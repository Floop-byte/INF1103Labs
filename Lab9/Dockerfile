FROM python:3.14.7

WORKDIR /app

COPY product.py can_be_shipped.py physical_product.py digital_product.py supplier.py inventory.py order.py order_line.py product_factory.py discount_strategy.py inventory_system.py inventory.json ./

CMD ["python", "inventory_system.py"]
