// WO-SARA-AM-004. Inputs: game binary and metadata (read only), existing LibCpp2IL.
// Output: stdout metadata evidence only. No game launch, asset changes or candidate build.
using System;
using System.IO;
using System.Reflection;
using System.Collections;
class SaraAm004Metadata {
 static object V(object o,string n) { if(o==null)return null;var t=o.GetType(); var f=t.GetField(n); if(f!=null)return f.GetValue(o);var p=t.GetProperty(n);return p==null?null:p.GetValue(o,null); }
 static void Dump(object o,string prefix,int depth) { if(o==null)return;Console.WriteLine(prefix+"TYPE="+o.GetType().FullName); foreach(var f in o.GetType().GetFields(BindingFlags.Instance|BindingFlags.Public)){var v=f.GetValue(o);Console.WriteLine(prefix+f.Name+"="+v);if(depth>0&&v!=null&&!v.GetType().IsPrimitive&&!(v is string)&&!(v is Array))Dump(v,prefix+"  ",depth-1);} }
 static void Main(string[] args) {
  var dir=@"C:\Users\udomp\Downloads\uabea-windows";
  AppDomain.CurrentDomain.AssemblyResolve+=(s,e)=>{var p=Path.Combine(dir,new AssemblyName(e.Name).Name+".dll");return File.Exists(p)?Assembly.LoadFrom(p):null;};
  var a=Assembly.LoadFrom(Path.Combine(dir,"LibCpp2IL.dll"));var main=a.GetType("LibCpp2IL.LibCpp2IlMain");
  var settings=main.GetField("Settings").GetValue(null);settings.GetType().GetField("AllowManualMetadataAndCodeRegInput").SetValue(settings,false);
  if(!(bool)main.GetMethod("LoadFromFile").Invoke(null,new object[]{args[0],args[1],new int[]{2020,3,47}}))throw new Exception("Load failed");
  var meta=main.GetField("TheMetadata").GetValue(null);
  foreach(var f in meta.GetType().GetFields())if(f.Name.ToLower().Contains("assembl")||f.Name.ToLower().Contains("image")){
   Console.WriteLine("METAFIELD="+f.Name);var arr=f.GetValue(meta) as IEnumerable;if(arr==null)continue;
   int index=0;foreach(var x in arr){if(index++==0)Dump(x,"SAMPLE ",2);var name=V(x,"Name");if(name==null){name=V(x,"AssemblyName");}
    if(name!=null&&name.ToString().Contains("TextMesh")){Console.WriteLine("MATCH="+name);Dump(x,"  ",2);}
   }
  }
  foreach(var t in (IEnumerable)V(meta,"typeDefs")) { var name=(string)V(t,"FullName");if(name=="TMPro.TMP_Settings"||name=="TMPro.TMP_TextParsingUtilities"||name=="TMPro.TMP_FontAsset"||name=="TMPro.TMP_FontFeatureTable"){
   Console.WriteLine("TYPE="+name);foreach(var f in (IEnumerable)V(t,"Fields"))Console.WriteLine(" FIELD="+V(f,"Name"));
  }}
 }
}
