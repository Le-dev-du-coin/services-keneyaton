from django.urls import path
from store.views import store, search, cart, checkout

urlpatterns = [
    # Boutique
    path("boutique/", store.store, name="boutique"),
    path("categorie/<slug:category_slug>/", store.store, name="category"),
    path(
        "detail-produit/<slug:product_slug>",
        store.product_detail,
        name="product-detail",
    ),
    # Panier
    path("mon-panier/", cart.cart, name="panier"),
    path("ajout-au-panier/", cart.update_item, name="ajout-au-panier"),
    path("passer-a-la-caise/", checkout.checkout, name="checkout"),
    # Recherche
    path("resultat-recherche/", search.search, name="search"),
]
