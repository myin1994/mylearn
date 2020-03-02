解决django自定义用户模型之前就已经数据迁移的BUG

Django建议我们对于AUTH_USER_MODEL参数的设置一定要在第一次数据库迁移之前就设置好，否则后续使用可能出现未知错误。

所以自定义用户模型以后，执行`python manage.py migrate`命令时，系统报错类似如下：

```bash
django.db.migrations.exceptions.InconsistentMigrationHistory: Migration reversion.0001_squashed_0004_auto_20160611_1202 is applied before its dependency users.0001_initial on database 'default'.
```

这是表示有一个叫reversion的子应用使用了原来的废弃的users模型，但是目前数据库已经设置了默认的子应用为`users`的模型了，所以产生了冲突。那么这种冲突，我们需要清除原来的迁移文件和数据库中的所有信息就可以解决了。

```
解决步骤：
1. 备份数据库，删除关于用户原来的数据表信息和表结构[如果刚开始开发，则直接清除库中所有数据表即可。]
2. 删除子应用users中migrations目录下除了__init__.py以外的所有迁移文件
3. 删除在django.contrib.admin和django.contrib.auth模块里面的migrations迁移文件，除了__init__.py
4. 删除在xadmin和reversion模块中的migrations的迁移文件，除了__init__.py。
5. 执行数据迁移，把备份数据，除了用户以外的全部恢复执行即可。
6. 使用manage.py createsuperuser创建管理员即可
```

