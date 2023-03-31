import odoorpc
import logging

logging.basicConfig()
logger = logging.getLogger('odoorpc')
logger.setLevel(logging.DEBUG)

# Prepare the connection to the server
odoo = odoorpc.ODOO('localhost', port=8069)

# Check available databases
print(odoo.db.list())

# Login
odoo.login('odoo', 'phanquocthinh@gmail.com', '1234')

# Current user
user = odoo.env.user
print(user.name)             # name of the user connected
print(user.company_id.name)  # the name of its company

# Simple 'raw' query
user_data = odoo.execute('res.users', 'read', [user.id])
print(user_data)

# Use all methods of a model
if 'sale.order' in odoo.env:
    Order = odoo.env['sale.order']
    order_ids = Order.search([])
    for order in Order.browse(order_ids):
        print(order.name)
        products = [line.product_id.name for line in order.order_line]
        print(products)

# Update data through a record
# user.name = "Brian Jones"
