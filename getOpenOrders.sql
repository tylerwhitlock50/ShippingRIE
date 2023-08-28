select
customer_order.ID,
customer_order.customer_id,
customer_order.customer_po_reference,
ifnull(cust_order_line.desired_ship_date, customer_order.desired_ship_date) as due_date,
cust_order_line.order_qty,
cust_order_line.shipped_qty,

from 
veca.dbo.customer_order customer_order inner join
    veca.dbo.cust_order_line cust_order_line on cust_order_line.cust_order_id = customer_order.id

where customer_order.status = 'R'
and customer_order.line_status = 'A'
and cust_order_line.order_qty - cust_order_line.shipped_qty > 0

