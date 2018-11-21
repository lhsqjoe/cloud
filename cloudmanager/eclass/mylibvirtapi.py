# -*- coding: utf-8 -*-
import libvirt
import sys


def createConnection(connUrl):
    conn = ''
    if connUrl == None:
        conn = libvirt.openReadOnly(None)
    else:
        conn = libvirt.open(connUrl)
    if conn == None:
        print("Failed to open connection to QEMU/KVM")
        sys.exit(1)
    else:
        print("----------------Connection is created successfully--------------------")
    return conn



def closeConnection(conn):
    print("----------close connection is invoked---------")

    try:
        conn.close()
    except:
        print("Failed to close the connection")
        return 1

    print("Connection is closed")



def getDomInfoByName(conn,name):
    print("---------------getDoInfoByName invoke--------------")
    print("----- get domain info by name -----")
    try:
        myDom = conn.lookupByName(name)
    except:
        print("Failed to find the domain with name", name)

        return 1

    # print("Dom id:{} name:{}".format(myDom.ID(),myDom.name())) #python3 str format
    # print("Dom state:{}".format(myDom.state(0)))
    # print("Dom info: {}".format(myDom.info()))
    # print("memory:{} MB".format((myDom.maxMemory() / 1024)))
    # print("memory status:{}".format(myDom.memoryStats()))
    # print("vCPUs:{}".format(myDom.maxVcpus()))
    # print("OSType:{}".format(myDom.OSType())) # return hvm
    # print("UUID:{}".format(myDom.UUIDString()))
    #print("XMLDesc:{}".format(myDom.XMLDesc())) # return vm xml
    return myDom

def getDomInfoByID(conn, id):
    print("")
    print("----- get domain info by ID -----")
    try:
        myDom = conn.lookupByID(id)
        return myDom
    except:
        print("Failed to find the domain with ID", id)
        return 1

    print("Domain id is ",myDom.ID()," ; Name is ",myDom.name())


def getLibvirtVersion(conn):
    return conn.getVersion()


def list_active_vms(conn):
    vms = []
    for id in conn.listDomainsID():
        vms.append(conn.lookupByID(id).name())
    return vms


def list_inactive_vms(conn):
    vms = []
    for id in conn.listDefinedDomains():
        vms.append(id)
    return vms


def list_vms(conn):
    '''
    Return a list of virtual machine names on the minion

    CLI Example::

        salt '*' virt.list_vms
    '''
    vms = []
    vms.extend(list_active_vms(conn))
    vms.extend(list_inactive_vms(conn))
    return vms



if __name__ == '__main__':
    connUrl = "qemu+tcp://10.10.203.162:16509/system"
    conn = createConnection(connUrl)
    #getDomInfoByID(conn,5003)
    myDom = getDomInfoByName(conn,'i-3D130800')

    #print(getLibvirtVersion(conn))


    #myDom.destroy(); #destroy dom
    #myDom.create() # boot dom

    vms = list_vms(conn)
    print(vms.__len__())
    for dom in vms:
        print("dom name:",dom)

