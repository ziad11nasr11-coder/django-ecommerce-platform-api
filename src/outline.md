🛒 E-commerce Platform (Django) – Project Outline

---

1) users

Models:

- User (Custom)
- Profile

Features:

- Register / Login / Logout
- Roles (Customer / Seller)
- Profile management

---

2) categories

Models:

- Category

Features:

- Create categories
- Nested categories (parent-child)
- Category filtering

---

3) products

Models:

- Product
- ProductImage

Features:

- Create products
- Assign seller
- Product images (multiple)
- Price / description / stock
- Link to category

---

4) inventory

Models:

- Inventory
- ProductVariant (optional)

Features:

- Track stock quantity
- Manage variants (size / color)
- Stock alerts

---

5) cart

Models:

- Cart
- CartItem

Features:

- Add products to cart
- Remove products
- Update quantity

---

6) orders

Models:

- Order
- OrderItem

Features:

- Create order from cart
- Order status:
  - Pending
  - Paid
  - Shipped
  - Delivered

---

7) payments

Models:

- Payment

Features:

- Payment processing
- Payment status
- Transaction tracking

---

8) shipping

Models:

- Address
- Shipment

Features:

- Store user addresses
- Shipping methods
- Delivery tracking

---

9) reviews

Models:

- Review

Features:

- Product rating (1–5)
- User comments

---

10) wishlist

Models:

- Wishlist

Features:

- Save products for later

---

11) coupons

Models:

- Coupon

Features:

- Discount codes
- Percentage / fixed discounts
- Expiration dates

---

12) search

Models:

- (No main model – يعتمد على products)

Features:

- Search products
- Filters:
  - Price
  - Category
  - Rating

---

13) notifications

Models:

- Notification

Features:

- In-app notifications
- Email notifications

---

14) core

Models:

- BaseModel (abstract)

Features:

- Shared utilities
- Common fields (created_at, updated_at)

---

🔗 Relationships:

User → Product (Seller)

Product → Category

Product → Inventory

Cart → User

CartItem → Product

Order → User

OrderItem → Product

User → Review → Product

User → Wishlist → Product

User → Payment → Order

Order → Shipment

---

🔄 User Flow:

Register → Browse Products → View Product
→ Add to Cart → Checkout → Payment
→ Order Created → Shipping
→ Receive Product → Leave Review

---
