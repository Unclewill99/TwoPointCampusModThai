using System;
using System.Linq;
using System.Reflection;
using System.Collections;
using System.IO;
class NativeMap {
 static object P(object o,string n){return o.GetType().GetProperty(n).GetValue(o,null);}
 static object F(object o,string n){return o.GetType().GetField(n).GetValue(o);}
 static void Main(string[] args) {
  var dir=@"C:\Users\udomp\Downloads\uabea-windows";
  AppDomain.CurrentDomain.AssemblyResolve += (s,e)=> {var p=Path.Combine(dir,new AssemblyName(e.Name).Name+".dll");return File.Exists(p)?Assembly.LoadFrom(p):null;};
  var a=Assembly.LoadFrom(Path.Combine(dir,"LibCpp2IL.dll"));var main=a.GetType("LibCpp2IL.LibCpp2IlMain");
  var settings=main.GetField("Settings").GetValue(null);settings.GetType().GetField("AllowManualMetadataAndCodeRegInput").SetValue(settings,false);
  if(!(bool)main.GetMethod("LoadFromFile").Invoke(null,new object[]{args[0],args[1],new int[]{2020,3,47}}))throw new Exception("Initialization failed");
  var meta=main.GetField("TheMetadata").GetValue(null);var binary=main.GetField("Binary").GetValue(null);
  if(args.Length>3){
   using(var output=new StreamWriter(args[2]+"/globals.tsv"))foreach(var line in File.ReadAllLines(args[3])){
    try{var addr=Convert.ToUInt64(line.Substring(2),16);var value=main.GetMethod("GetAnyGlobalByAddress").Invoke(null,new object[]{addr});if(value!=null){output.WriteLine(line+"\t"+value);foreach(var prop in value.GetType().GetProperties()){try{output.WriteLine("  "+prop.Name+"="+prop.GetValue(value,null));}catch{}}}}catch{}
   }
   return;
  }
  using(var modules=new StreamWriter(args[2]+"/modules.tsv")) {
   foreach(var t in (IEnumerable)F(meta,"typeDefs")) {
    var name=(string)P(t,"FullName");if(name!="TPC.PreferencesPanelVideo" && name!="TPC.TooltipSpawner" && name!="TPC.TooltipManager")continue;
    var module=P(t,"CodeGenModule");modules.WriteLine(name+"\t"+P(module,"Name")+"\t"+((ulong)F(module,"methodPointers")).ToString("X")+"\t"+F(module,"methodPointerCount"));
   }
  }
  using(var output=new StreamWriter(args[2]+"/methods.tsv")){
   foreach(var m in (IEnumerable)F(meta,"methodDefs")){
    try {var ptr=(ulong)P(m,"MethodPointer");if(ptr==0)continue;var t=P(m,"DeclaringType");output.WriteLine(ptr.ToString("X")+"\t"+P(m,"MethodOffsetInFile")+"\t"+((uint)F(m,"token")).ToString("X")+"\t"+P(t,"FullName")+"::"+P(m,"Name"));}catch(Exception){}
   }
  }
  using(var output=new StreamWriter(args[2]+"/fields.tsv")){
   foreach(var t in (IEnumerable)F(meta,"typeDefs")){
    var name=(string)P(t,"FullName");if(!(name.Contains("PreferencesPanelVideo")||name.Contains("TooltipSpawner")||name=="TPC.TooltipManager"||name=="TPS.Core.Input.InputManager"))continue;
    var fields=(Array)P(t,"Fields");int local=0;
    foreach(var f in fields){var index=(int)F(t,"firstFieldIdx")+local;var offset=binary.GetType().GetMethod("GetFieldOffsetFromIndex").Invoke(binary,new object[]{(int)P(t,"TypeIndex"),local,index,false,false});output.WriteLine(name+"\t"+P(f,"Name")+"\t"+offset);local++;}
   }
  }
 }
}
