# LDAP connection to AD server
import ldap3

def connect_to_ldap(server, user, password):
    """
    Connect to the LDAP server and return the connection object.
    
    :param server: LDAP server URL
    :param user: Username for authentication
    :param password: Password for authentication
    :return: LDAP connection object
    """
    try:
        # Initialize the LDAP connection
        conn = ldap3.initialize(server)

        # Bind to the server with user credentials
        conn.simple_bind_s(user, password)
        print("LDAP connection established successfully.")
        return conn
    except ldap3.LDAPError as e:
        print(f"Error connecting to LDAP server: {e}")
        return None