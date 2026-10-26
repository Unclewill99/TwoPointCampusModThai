using System;
using System.IO;
using System.Reflection;
using System.Collections;
class InspectNewsMetadata {
 static object P(object o,string n){return o.GetType().GetProperty(n).GetValue(o,null);}
 static object F(object o,string n){return o.GetType().GetField(n).GetValue(o);}
 static void Main(string[] args) {
  var dir=@"C:\Users\udomp\Downloads\uabea-windows";
  AppDomain.CurrentDomain.AssemblyResolve+=(s,e)=>{var p=Path.Combine(dir,new AssemblyName(e.Name).Name+".dll");return File.Exists(p)?Assembly.LoadFrom(p):null;};
  var a=Assembly.LoadFrom(Path.Combine(dir,"LibCpp2IL.dll"));var main=a.GetType("LibCpp2IL.LibCpp2IlMain");
  var settings=main.GetField("Settings").GetValue(null);settings.GetType().GetField("AllowManualMetadataAndCodeRegInput").SetValue(settings,false);
  if(!(bool)main.GetMethod("LoadFromFile").Invoke(null,new object[]{args[0],args[1],new int[]{2020,3,47}}))throw new Exception("Initialization failed");
  var meta=main.GetField("TheMetadata").GetValue(null);var binary=main.GetField("Binary").GetValue(null);
  foreach(var t in (IEnumerable)F(meta,"typeDefs")) {
   var name=(string)P(t,"FullName");if(!(name.Contains("News") && (name.StartsWith("TPC.")||name.StartsWith("Frontend"))))continue;
   Console.WriteLine("TYPE "+name);
   int local=0;foreach(var f in (IEnumerable)P(t,"Fields")) {
    var index=(int)F(t,"firstFieldIdx")+local;
    var offset=binary.GetType().GetMethod("GetFieldOffsetFromIndex").Invoke(binary,new object[]{(int)P(t,"TypeIndex"),local,index,false,false});
    Console.WriteLine("FIELD "+P(f,"Name")+" "+offset);local++;
   }
  }
 }
}
