'''
/********************************************************************
*	Module:			regd.defs
*
*	Created:		Jul 5, 2015
*
*	Abstract:		Definitions.
*
*	Author:			Albert Berger [ alberger@gmail.com ].
*		
*********************************************************************/
'''
__lastedited__="2015-07-11 20:25:28"

VERSION = ( 0, 6, 'pre0', 17 )
__version__ = '.'.join( map( str, VERSION[0:3] ) )
__description__ = 'Registry daemon and data cache'
__author__ = 'Albert Berger'
__author_email__ = 'nbdspcl@gmail.com'
__homepage__ = 'https://github.com/nbdsp/regd'
__license__ = 'GPL'
rversion = '.'.join(map(str, VERSION[0:3]))+ '.r' + str(VERSION[3])

sockname 			= 'regd.sock'
APPNAME 			= "regd"
# Default command for loading secure tokens
READ_ENCFILE_CMD 	= "gpg --textmode -d FILENAME"
	
# Privacy levels
PL_PRIVATE			= 1
PL_PUBLIC_READ		= 2
PL_PUBLIC			= 3

homedir 			= None
confdir 			= None

# Commands
START_SERVER		= "start"
STOP_SERVER			= "stop"
RESTART_SERVER		= "restart"
CHECK_SERVER		= "check"
REPORT				= "what"
LIST				= "ls"
ADD_TOKEN 			= "add"
ADD_TOKEN_SEC		= "add_sec"
LOAD_FILE 			= "load_file"
LOAD_FILE_SEC 		= "load_file_sec"
GET_TOKEN 			= "get"
GET_TOKEN_SEC		= "get_sec"
REMOVE_TOKEN		= "rm"
REMOVE_TOKEN_SEC	= "remove_sec"
REMOVE_SECTION		= "rmsect"
REMOVE_SECTION_SEC	= "remove_section_sec"
CLEAR_SEC			= "clear_sec"
CLEAR_SESSION		= "clear_session"
SHOW_LOG			= "show_log"
TEST_START			= "test_start"
TEST_CONFIGURE		= "test_configure"
TEST_MULTIUSER_BEGIN= "test_multiuser_begin"
TEST_MULTIUSER_END 	= "test_multiuser_end"
HELP 				= "help"
VERS				= "version"

# Command options
DEST				= "dest"
SESSION				= "session"
PERS				= "pers"
ALL					= "all"
TREE				= "tree"
FORCE				= "force"
SERVER_SIDE			= "server_side"
FROM_PARS			= "from_pars"

# Report ("what") options
ACCESS 				= "access"
STAT				= "stat"
DATAFILE			= "datafile"
VERS 

# Command groups
all_cmds = ( START_SERVER, STOP_SERVER, RESTART_SERVER, CHECK_SERVER, REPORT,
			LIST, ADD_TOKEN, ADD_TOKEN_SEC, LOAD_FILE, LOAD_FILE_SEC, GET_TOKEN, GET_TOKEN_SEC,
			REMOVE_TOKEN, REMOVE_TOKEN_SEC, REMOVE_SECTION,
			REMOVE_SECTION_SEC, CLEAR_SEC, CLEAR_SESSION, TEST_START, TEST_CONFIGURE,
			TEST_MULTIUSER_BEGIN, TEST_MULTIUSER_END, VERS, HELP)
pubread_cmds = ( CHECK_SERVER, LIST, GET_TOKEN )
secure_cmds = ( START_SERVER, STOP_SERVER, RESTART_SERVER, REPORT, 
			ADD_TOKEN_SEC, GET_TOKEN_SEC, LOAD_FILE_SEC, REMOVE_TOKEN_SEC, REMOVE_SECTION_SEC, 
			CLEAR_SEC)
pers_opts = (PERS)
local_cmds = (TEST_START, TEST_CONFIGURE, TEST_MULTIUSER_BEGIN, TEST_MULTIUSER_END)
# For executing these commands on server they must come with --server-side switch 
nonlocal_cmds = (SHOW_LOG, VERS)
cmd_opts = ( DEST, SESSION, PERS, ALL, TREE, FORCE, SERVER_SIDE, FROM_PARS )
rep_opts = (ACCESS, STAT, DATAFILE)