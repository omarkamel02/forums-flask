import copy
class BaseStore(object):

    def __init__(self, data_provider, last_id):
        self._data_provider = data_provider
        self.last_id = last_id
    def get_all(self):
        return self._data_provider

    def add(self, item_instance):
        item_instance.id = self.last_id
        self._data_provider.append(item_instance)
        #print(item_instance.id)
        #print item_instance.id
        self.last_id+=1

    def get_by_id(self, id):
        for mem in self.get_all() :
            if mem.id == id:
                return mem
        return 0

    def update(self, instance):
        name=self.get_by_id(instance.id)
        index=self._data_provider.index(name)

        self._data_provider[index]=instance

    def delete(self, id):
        # delete member by id
        name=self.get_by_id(id)
        self._data_provider.remove(name)

    def entity_exists(self, instance):
        if self.get_by_id(member.id) != 0:
            return True
        else :
            return False


class MemberStore(BaseStore):
    members = []
    last_id = 1

    def __init__(self):
        super(MemberStore, self).__init__(MemberStore.members, MemberStore.last_id)


    def get_members_with_posts(self,all_posts) :
        return_list=[]
        allmembers=self.get_all()

        for mem in allmembers :
            #print mem.id
            for post in all_posts:
                if post.member_id==mem.id :

                    mem.posts.append(post)

        return self.get_all()


    def get_top_two(self,all_posts):
        list=self.get_members_with_posts(all_posts)
        list.sort(key=lambda member: len(member.posts), reverse=True)
        return list[:2]

    def get_by_name (self,name):
        all_members = self.get_all()
        for member in all_members:
            if member.name == member_name:
                yield member

class PostsStore(BaseStore):
    posts=[]
    last_id=1

    def __init__(self):
        super(PostsStore, self).__init__(PostsStore.posts,PostsStore.last_id)
    def get_posts_by_date(self):
        all_posts=self.get_all()
        all_posts.sort(key=lambda post: post.date)
        return posts_sorted_byDate
