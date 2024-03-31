var UserGroupManager = {
    addUserToGroup: function(groupId, userId) {
        var gr = new GlideRecord('sys_user_grmember');
        gr.initialize();
        gr.setValue('group', groupId);
        gr.setValue('user', userId);
        gr.insert();
        return 'User added to group successfully';
    }
};