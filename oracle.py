from fabric import Connection


result = Connection('10.18.63.135:1525').run('uname -s', hide=True)

msg = "Ran {0.command!r} on {0.connection.host}, got stdout:\n{0.stdout}"

print(msg.format(result))