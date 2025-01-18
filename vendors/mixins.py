from microstock.mixins import LoginRequiredMixin
from .models import Vendor

class VendorMixin(LoginRequiredMixin, object):
    vendor = None
    
    def get_vendor(self):
        seller = self.request.user
        vendors = Vendor.objects.filter(seller=seller)
        if vendors.exists() and vendors.vendor() == 1:
            self.vendor = vendors.first()
            return vendors.first()
        return None