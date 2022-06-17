from django.contrib import admin
from buildings.models import Building, BuildingImage, Address, Floor, Room, MyEvent


class BuildingImageInline(admin.StackedInline):
    model = BuildingImage


class AddressInline(admin.StackedInline):
    model = Address


class FloorInline(admin.StackedInline):
    model = Floor


class RoomInline(admin.StackedInline):
    model = Room


class BuildingAdminConfig(admin.ModelAdmin):
    model = Building
    inlines = [BuildingImageInline, AddressInline, FloorInline]
    list_display = ["building_name", "company", "is_active", "slug", "created_at"]
    list_filter = ["building_name", "company", "is_active"]
    list_editable = ["is_active"]

    prepopulated_fields = {"slug": ("building_name",)}


class FloorAdminConfig(admin.ModelAdmin):
    model = Floor
    list_display = ["title", "level", "created_at"]
    inlines = [RoomInline]


class RoomAdminConfig(admin.ModelAdmin):
    model = Room
    list_display = [
        "title",
        "capacity",
        "permission_level",
        "created_at",
    ]


class MyEventAdminConfig(admin.ModelAdmin):
    model = MyEvent

    list_display = ["id", "title", "room"]


admin.site.register(Building, BuildingAdminConfig)
admin.site.register(Floor, FloorAdminConfig)
admin.site.register(Room, RoomAdminConfig)
admin.site.register(MyEvent, MyEventAdminConfig)
