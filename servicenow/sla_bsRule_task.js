(function executeRule(current, previous /*null when async*/) {

	// Add your code here

	gs.addInfoMessage("the sys_d of the user made a comment is: " + current.sys_updated_by + "and the assignment group is " + current.assignment_group);
	var groupId = current.assignment_group;
	var commenter = current.sys_updated_by;
	var userComment = new GlideRecord('sys_user');
	userComment.addQuery('user_name', commenter);
	userComment.query();
	if(userComment.next()){
		var userId = userComment.sys_id;
	}
	var userGroupGr = new GlideRecord('sys_user_grmember');
	userGroupGr.addQuery('name', userId);
	userGroupGr.addQuery('group', groupId);
	userGroupGr.query();
	if(userGroupGr.next()){
		current.assigned_to = commenter;
		current.state = '2';
	}

})(current, previous);