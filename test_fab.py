
from fabric import Connection


c = Connection('10.18.63.135:22','im',connect_kwargs={
        "password": "im",}).run("ls", hide=True)

#'sqlplus unouser/unopass@vas-scan:1525/imconfig'
msg = "Ran {0.command!r} on {0.connection.host}, got stdout:\n{0.stdout}"

print(c)