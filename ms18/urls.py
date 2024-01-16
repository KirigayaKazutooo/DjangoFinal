from django.urls import path
<<<<<<< HEAD
from .views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView, SupplierListView, SupplierCreateView,admin_review_orders, admin_approve_order, admin_reject_order
from .views import add_supplier_to_product, view_requisitions
from .views import admin_review_requisitions, admin_approve_requisition, admin_reject_requisition
=======
from .views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView, SupplierListView, SupplierCreateView,admin_review_orders, admin_approve_order, admin_reject_order, RequestedProdView, generate_receipt
from .views import add_supplier_to_product, add_to_req, view_requisitions, approve_requisition, reject_requisition
>>>>>>> 2fca8341db61de77afb006be2367ad46b9e2ff42
from . import views


urlpatterns = [
    path('', ProductListView.as_view(), name='ms18-home'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('product/new/', ProductCreateView.as_view(), name='product-create'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product-update'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product-delete'),
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.cart, name='cart'),
   #path('remove/<int:cart_id>/', views.remove_from_cart, name='remove-from-cart'),
    path('suppliers/', SupplierListView.as_view(), name='supplier-list'),
    path('add-supplier-to-product/<int:product_id>/', add_supplier_to_product, name='add-supplier-to-product'),
   #path('clear-cart/', views.clear_cart, name='clear-cart'),
   #path('about/cart/', views.cart_view, name='about-cart'),  # Add a URL pattern for the about/cart page
    path('supplier/new/', SupplierCreateView.as_view(), name='supplier-create'),
    path('purchaseOrder/', views.about, name='ms18-about'),
    path('admin/review-orders/', admin_review_orders, name='admin_review_orders'),
    path('admin/approve-order/<int:order_id>/', admin_approve_order, name='admin_approve_order'),
    path('admin/reject-order/<int:order_id>/', admin_reject_order, name='admin_reject_order'),
<<<<<<< HEAD
    path('requisition/', view_requisitions, name='requisition'),  # Add this line
    #new
    path('admin_review_requisitions/', views.admin_review_requisitions, name='admin_review_requisitions'),
    path('admin_approve_requisition/<int:requisition_id>/', views.admin_approve_requisition, name='admin_approve_requisition'),
    path('admin_reject_requisition/<int:requisition_id>/', views.admin_reject_requisition, name='admin_reject_requisition'),
    path('admin/review-requisitions/', admin_review_requisitions, name='admin_review_requisitions'),
    path('admin/approve-requisition/<int:requisition_id>/', admin_approve_requisition, name='admin_approve_requisition'),
    path('admin/reject-requisition/<int:requisition_id>/', admin_reject_requisition, name='admin_reject_requisition'),
=======
    path('generate-receipt/', generate_receipt, name='generate-receipt'),
    path('AddRequisition/', views.add_requisitions, name='add-requisition'),  
    path('add-to-req/', views.add_to_req, name='add_to_req'),
    path('ViewRequisition/', views.view_requisitions, name='view-requisitions'), 
    path('approve_requisition/<int:req_id>/', views.approve_requisition, name='approve_requisition'),
    path('reject_requisition/<int:req_id>/', views.reject_requisition, name='reject_requisition'),
    path('requested_prod/<int:pk>/', views.RequestedProdView, name='requested-product-view'),
>>>>>>> 2fca8341db61de77afb006be2367ad46b9e2ff42
]

