var scriptIncludeName = "CatalogItemVersioningService";
var scriptInclude = new GlideRecord('sys_script_include');
scriptInclude.addQeury('name', scriptIncludeName)
scriptInclude.query();
if(scriptInclude.next()) {
    gs.info("The script in the script include: " + scriptInclude.getValue('script'));
} else {
    gs.info("Script include not found");
}