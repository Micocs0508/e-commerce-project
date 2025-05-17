from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivymd.uix.list import OneLineListItem
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField

import os
from database import Database

# main.py - KivyMD E-commerce App

# This file contains the main application code for the PUP MERCH SHOP.
# It defines the UI screens, navigation, and core app logic using KivyMD framework.

# To edit this project:
# - UI layout is defined in the KV string using Kivy language.
# - Screens are implemented as Python classes inheriting from Screen.
# - Product images are loaded from the 'product_images' folder located alongside this file.
# - To add or modify products, update the 'products' list in ProductListScreen.on_enter method.
# - User authentication is handled via SignInScreen and SignUpScreen classes.
# - Cart and checkout functionality are implemented in CartScreen and CheckoutScreen.
# - User list is displayed in UsersScreen.
# - To add new features, create new screens and register them in the ScreenManager in the KV string.
# - For styling, modify the KV string or add custom widgets as needed.

KV = '''
ScreenManager:
    HomeScreen:
    SignInScreen:
    SignUpScreen:
    ProductListScreen:
    ProductDetailScreen:
    CartScreen:
    CheckoutScreen:
    UsersScreen:

<HomeScreen>:
    name: 'home'
    MDBoxLayout:
        orientation: 'vertical'
        size_hint_x: 0.8
        pos_hint: {'center_x': 0.5}
        MDLabel:
            text: 'Welcome to PUP MERCH SHOP'
            halign: 'center'
            valign: 'top'
            font_style: 'H4'
            size_hint_y: None
            height: self.texture_size[1] + dp(20)
            padding: 0, dp(20)
        BoxLayout:
            orientation: 'vertical'
            size_hint_y: None
            height: self.minimum_height
            spacing: dp(10)
            MDRaisedButton:
                text: 'Sign In'
                size_hint_x: 0.6
                pos_hint: {'center_x': 0.5}
                on_release:
                    root.manager.current = 'signin'
            MDRaisedButton:
                text: 'Sign Up'
                size_hint_x: 0.6
                pos_hint: {'center_x': 0.5}
                on_release:
                    root.manager.current = 'signup'
            MDRaisedButton:
                text: 'Go to Products'
                size_hint_x: 0.6
                pos_hint: {'center_x': 0.5}
                on_release:
                    root.manager.current = 'product_list'
            MDRaisedButton:
                text: 'View Users'
                size_hint_x: 0.6
                pos_hint: {'center_x': 0.5}
                on_release:
                    root.manager.current = 'users'

<SignInScreen>:
    name: 'signin'
    MDBoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(20)
        size_hint_x: 0.8
        pos_hint: {'center_x': 0.5}
        MDLabel:
            text: 'Sign In'
            halign: 'center'
            font_style: 'H4'
        MDTextField:
            id: email
            hint_text: 'Email'
            helper_text_mode: 'on_focus'
            required: True
            pos_hint: {'center_x': 0.5}
            size_hint_x: 0.8
        MDTextField:
            id: password
            hint_text: 'Password'
            password: True
            required: True
            pos_hint: {'center_x': 0.5}
            size_hint_x: 0.8
        MDRaisedButton:
            text: 'Sign In'
            pos_hint: {'center_x': 0.5}
            on_release:
                root.sign_in()
        MDTextButton:
            text: 'Back to Home'
            pos_hint: {'center_x': 0.5}
            on_release:
                root.manager.current = 'home'

<SignUpScreen>:
    name: 'signup'
    MDBoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(20)
        size_hint_x: 0.8
        pos_hint: {'center_x': 0.5}
        MDLabel:
            text: 'Sign Up'
            halign: 'center'
            font_style: 'H4'
        MDTextField:
            id: email
            hint_text: 'Email'
            helper_text_mode: 'on_focus'
            required: True
            pos_hint: {'center_x': 0.5}
            size_hint_x: 0.8
        MDTextField:
            id: password
            hint_text: 'Password'
            password: True
            required: True
            pos_hint: {'center_x': 0.5}
            size_hint_x: 0.8
        MDTextField:
            id: confirm_password
            hint_text: 'Confirm Password'
            password: True
            required: True
            pos_hint: {'center_x': 0.5}
            size_hint_x: 0.8
        MDRaisedButton:
            text: 'Sign Up'
            pos_hint: {'center_x': 0.5}
            on_release:
                root.sign_up()
        MDTextButton:
            text: 'Back to Home'
            pos_hint: {'center_x': 0.5}
            on_release:
                root.manager.current = 'home'

<ProductListScreen>:
    name: 'product_list'
    MDBoxLayout:
        orientation: 'vertical'
        size_hint_x: 0.8
        pos_hint: {'center_x': 0.5}
        MDLabel:
            text: 'Product List'
            halign: 'center'
            font_style: 'H5'
            size_hint_y: None
            height: self.texture_size[1] + dp(20)
        ScrollView:
            MDList:
                id: product_list
        MDRaisedButton:
            text: 'Back to Home'
            pos_hint: {'center_x': 0.5}
            on_release:
                root.manager.current = 'home'

<ProductDetailScreen>:
    name: 'product_detail'
    MDBoxLayout:
        orientation: 'vertical'
        size_hint_x: 0.8
        pos_hint: {'center_x': 0.5}
        Image:
            id: product_image
            size_hint_y: 0.5
            allow_stretch: True
            keep_ratio: True
        MDLabel:
            id: product_name
            text: 'Product Detail'
            halign: 'center'
            font_style: 'H5'
            size_hint_y: None
            height: self.texture_size[1] + dp(20)
        MDLabel:
            id: product_description
            text: 'Description goes here'
            halign: 'center'
        MDRaisedButton:
            text: 'Add to Cart'
            pos_hint: {'center_x': 0.5}
            on_release:
                root.add_to_cart()
        MDRaisedButton:
            text: 'Back to Products'
            pos_hint: {'center_x': 0.5}
            on_release:
                root.manager.current = 'product_list'

<CartScreen>:
    name: 'cart'
    MDBoxLayout:
        orientation: 'vertical'
        size_hint_x: 0.8
        pos_hint: {'center_x': 0.5}
        MDLabel:
            text: 'Your Cart'
            halign: 'center'
            font_style: 'H5'
            size_hint_y: None
            height: self.texture_size[1] + dp(20)
        ScrollView:
            MDList:
                id: cart_list
        MDRaisedButton:
            text: 'Checkout'
            pos_hint: {'center_x': 0.5}
            on_release:
                root.manager.current = 'checkout'
        MDRaisedButton:
            text: 'Back to Home'
            pos_hint: {'center_x': 0.5}
            on_release:
                root.manager.current = 'home'

<CheckoutScreen>:
    name: 'checkout'
    MDBoxLayout:
        orientation: 'vertical'
        size_hint_x: 0.8
        pos_hint: {'center_x': 0.5}
        MDLabel:
            text: 'Checkout'
            halign: 'center'
            font_style: 'H5'
            size_hint_y: None
            height: self.texture_size[1] + dp(20)
        MDLabel:
            text: 'Thank you for your purchase!'
            halign: 'center'
        MDRaisedButton:
            text: 'Back to Home'
            pos_hint: {'center_x': 0.5}
            on_release:
                root.manager.current = 'home'

<UsersScreen>:
    name: 'users'
    MDBoxLayout:
        orientation: 'vertical'
        size_hint_x: 0.8
        pos_hint: {'center_x': 0.5}
        ScrollView:
            MDList:
                id: user_list
        MDRaisedButton:
            text: 'Back to Home'
            size_hint_x: 0.6
            pos_hint: {'center_x': 0.5}
            on_release:
                root.manager.current = 'home'
'''

class HomeScreen(Screen):
    pass

class UsersScreen(Screen):
    def on_enter(self):
        self.ids.user_list.clear_widgets()
        app = MDApp.get_running_app()
        users = app.db.get_all_users()
        for user in users:
            user_id, email = user
            self.ids.user_list.add_widget(OneLineListItem(text=f"{user_id}: {email}"))

from kivymd.app import MDApp

class SignInScreen(Screen):
    def sign_in(self):
        from kivymd.toast import toast
        email = self.ids.email.text
        password = self.ids.password.text
        if not email or not password:
            toast("Please enter email and password")
            return
        app = MDApp.get_running_app()
        if not app.db.verify_user(email, password):
            toast("Invalid email or password")
            return
        toast(f"Signed in as {email}")
        app.signed_in = True
        self.manager.current = 'product_list'

class SignUpScreen(Screen):
    def sign_up(self):
        from kivymd.toast import toast
        email = self.ids.email.text
        password = self.ids.password.text
        confirm_password = self.ids.confirm_password.text
        if not email or not password or not confirm_password:
            toast("Please fill all fields")
            return
        if password != confirm_password:
            toast("Passwords do not match")
            return
        app = MDApp.get_running_app()
        if not app.db.add_user(email, password):
            toast("Email already exists")
            return
        toast(f"Account created for {email}")
        self.manager.current = 'product_list'

class ProductListScreen(Screen):
    def on_enter(self):
        product_list = self.ids.product_list
        product_list.clear_widgets()
        # Sample products
        base_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'product_images')
        products = [
            {'name': 'T-Shirts', 'description': 'Comfortable and stylish t-shirts', 'image': os.path.join(base_path, 'T-SHIRT_1.jpg')},
            {'name': 'Lanyards', 'description': 'Durable and colorful lanyards', 'image': os.path.join(base_path, 'LANYARD_1.jpg')},
            {'name': 'Silhouette Beep Skin', 'description': 'Protective and sleek silhouette beep skin', 'image': os.path.join(base_path, 'SILHOUETTE_BEEP_SKIN.jpg')},
            {'name': 'Reversible Lanyards', 'description': 'Lanyards with reversible designs', 'image': os.path.join(base_path, 'REVIRSABLE_LANYARDS.jpg')},
            {'name': 'Stickers', 'description': 'Fun and vibrant stickers', 'image': os.path.join(base_path, 'COLLAB_STICKERS.jpg')},
        ]
        from kivymd.uix.list import OneLineAvatarListItem, ImageLeftWidget
        for product in products:
            item = OneLineAvatarListItem(text=product['name'])
            if product.get('image'):
                image = ImageLeftWidget(source=product['image'])
                item.add_widget(image)
            item.bind(on_release=lambda x, p=product: self.show_product_detail(p))
            product_list.add_widget(item)

    def show_product_detail(self, product):
        detail_screen = self.manager.get_screen('product_detail')
        detail_screen.ids.product_name.text = product['name']
        detail_screen.ids.product_description.text = product['description']
        detail_screen.ids.product_image.source = product.get('image', '')
        self.manager.current = 'product_detail'

from kivymd.app import MDApp

class ProductDetailScreen(Screen):
    def add_to_cart(self):
        app = MDApp.get_running_app()
        if not app.signed_in:
            from kivymd.toast import toast
            toast("Please sign in to add products to cart")
            self.manager.current = 'signin'
            return
        cart_screen = self.manager.get_screen('cart')
        cart_list = cart_screen.ids.cart_list
        product_name = self.ids.product_name.text
        cart_list.add_widget(OneLineListItem(text=product_name))
        app.cart.append(product_name)
        self.manager.current = 'cart'

class CartScreen(Screen):
    def on_enter(self):
        cart_list = self.ids.cart_list
        cart_list.clear_widgets()
        app = MDApp.get_running_app()
        for product_name in app.cart:
            cart_list.add_widget(OneLineListItem(text=product_name))

class CheckoutScreen(Screen):
    def on_enter(self):
        app = MDApp.get_running_app()
        app.cart.clear()

class EcommerceApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.signed_in = False
        self.db = Database()
        self.cart = []

    def build(self):
        return Builder.load_string(KV)


if __name__ == '__main__':
    EcommerceApp().run()
