import sqlite3

conn = sqlite3.connect('Assigment_15_1.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts') # Creating new table every time the code runs

cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue

    # Extracting the emails from the lines
    line_pieces = line.split()
    email = line_pieces[1]
    
    # Extracting the orgs from the emails
    email_pieces = email.split("@")
    organisation = email_pieces[1]
    
    # Retrieving data
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (organisation,)) # "organisation" is in a tuple
    row = cur.fetchone()
    if row is None:
        cur.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (organisation,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (organisation,))
conn.commit()

# https://www.sqlite.org/lang_select.html
# Retrieving the whole database:
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'
# There is no "fetchall" command here like in row26 because the default is to fetch everything with a SELECT command.

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
