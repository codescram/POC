from fastapi import APIRouter


router = APIRouter(prefix="/products", tags=["products"])

products = [
    { 
        "id":20,
        "name":"Brush",
        "price":"30",
        "image_url":"https://www.icpahealth.com/wp-content/uploads/2018/05/01_CLINSODENT-BRUSH.png"
    },
    {
        "id":20,
        "name":"Brush",
        "price":"30",
        "image_url":"https://www.icpahealth.com/wp-content/uploads/2018/05/01_CLINSODENT-BRUSH.png"
    }
]


@router.get("/")
def get_products():
    return products