# coding:utf-8

class RET:
    OK                  = "0"
    DBERR               = "4001"
    NODATA              = "4002"
    DATAEXIST           = "4003"
    DATAERR             = "4004"
    SESSIONERR          = "4101"
    LOGINERR            = "4102"
    PARAMERR            = "4103"
    USERERR             = "4104"
    ROLEERR             = "4105"
    PWDERR              = "4106"
    REQERR              = "4201"
    IPERR               = "4202"
    THIRDERR            = "4301"
    IOERR               = "4302"
    SERVERERR           = "4500"
    UNKOWNERR           = "4501"

error_map = {
    RET.OK                    : u"Success",
    RET.DBERR                 : u"Database Error",
    RET.NODATA                : u"No Data",
    RET.DATAEXIST             : u"Data Exists",
    RET.DATAERR               : u"Data Error",
    RET.SESSIONERR            : u"Session Error / Not Logged in",
    RET.LOGINERR              : u"Login Failed",
    RET.PARAMERR              : u"Parameter Erro",
    RET.USERERR               : u"Non-exist User / Not activated User",
    RET.ROLEERR               : u"User Role Error",
    RET.PWDERR                : u"Wrong password",
    RET.REQERR                : u"Illegal requests or limited number of requests",
    RET.IPERR                 : u"Restricted IP",
    RET.THIRDERR              : u"Errors in third-party systems",
    RET.IOERR                 : u"Read and write errors in the file",
    RET.SERVERERR             : u"Internal Error",
    RET.UNKOWNERR             : u"Unknown Error",
}
