(function process(/*RESTAPIRequest*/ request, /*RESTAPIResponse*/ response) {

    // implement resource here
	function buildJSON(record){
		var knowledgeJSON = {
			label: record.getValue('label'),
			name: record.getValue('label'),
			children: []
		};
		return knowledgeJSON;
	}


	var body = [];
	var count = 0;
	var rootKnowledge = new GlideRecord('kb_category');
	rootKnowledge.query();
	while(rootKnowledge.next()){
		body.push(buildJSON(rootKnowledge)); 

		var subKnowledge = new GlideRecord('kb_category');
		subKnowledge.addQuery('parent_id', rootKnowledge.sys_id);
		subKnowledge.query();
		while(subKnowledge.next()){
			body[count].children.push(buildJSON(subKnowledge));
		}
		count ++;
	}	
	response.setBody(body);


})(request, response);