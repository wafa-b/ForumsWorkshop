class MemberStore:

    members = []
    last_id = 1

    def get_all(self):
        return MemberStore.members

    def add(self,member):
        member.id = MemberStore.last_id
        MemberStore.members.append(member)
        MemberStore.last_id += 1

    def get_by_id(self,id):
        all_members = self.get_all()
        for member in all_members:
            if member.id == id:
                return  member

    def update(self,member):
        member = self.get_by_id(id)
        return  member

    def delete(self,id):
      member = self.get_by_id(id)
      MemberStore.members.remove(member)

    def entity_exists(self,member):
        if self.get_by_id(member.id):
            return True
        return  False

    def get_by_name(self, member_name):
        all_members = self.get_all()
        for member in all_members:
            if member.name == member_name:
                return  member



class PostStore:

    posts = []
    last_id = 1

    def get_all(self):
        return PostStore.posts

    def add(self,post):
        post.id = PostStore.last_id
        PostStore.posts.append(post)
        PostStore.last_id += 1

    def get_by_id(self,id):
        all_posts = self.get_all()
        for post in all_posts:
            if post.id == id:
                return  post

    def update(self,post):
        post = self.get_by_id(id)
        return  post

    def delete(self,id):
        post = self.get_by_id(id)
        PostStore.posts.remove(post)

    def entity_exists(self,post):
        if self.get_by_id(post.id):
            return True
        return  False


    def get_by_name(self, post_name):
        all_posts = self.get_all()
        for post in all_posts:
            if post.name == post_name:
                return  post
