# * MyMethod
# * Impjhtant informatiun is highlighted
# ! Deprecated nethod? do not use
# ? Should this method be exposed in the pubic API?
#  TODO: refactor this method so that conforms to the API
# * @param myParam The parameter for this method
# kfdjdksljfskdjf
# ! kfdjdksljfskdjf

# class Post(models.Model):
#     title = models.CharField(max_length=200)
#     pub_date = models.DateTimeField()
#     text = models.TextField()
#     slug = models.SlugField(max_length=40, unique=True)

    # def get_absolute_url(self):
    #     return "/{}/{}/{}/".format(self.pub_date.year, 
    #                                self.pub_date.month, 
    #                                self.slug)

#     def __unicode__(self):
#         return self.title

#     class Meta:
#         ordering = ['-pub_date']


class Employee:
    name = "Nic"
    last_name = "Vas"



    
class TestEmployee(Employee):
    name = Employee
    last_name = Employee()
    model = Employee
    obj = Employee()

    def show(self):
        print('name:{} last:{} model:{} obj{}'.format(
            self.name, self.last_name, self.model, self.obj)
        )

user = Employee
obj_user = Employee()
user_t = TestEmployee
user_mt =TestEmployee()
print(user is obj_user)
print(user, obj_user)
print(user_t.show)
print(user_mt.show)
