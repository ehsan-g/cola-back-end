from django.contrib import admin
from buildings.models import (
    Building,
    FloorLayout,
    BuildingImage,
    Address,
    Floor,
    Room,
    MyEvent,
)
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class BuildingImageInline(admin.StackedInline):
    model = BuildingImage


class AddressInline(admin.StackedInline):
    model = Address


class FloorInline(admin.StackedInline):
    model = Floor


class RoomInline(admin.StackedInline):
    model = Room


class LayoutResource(resources.ModelResource):
    class Meta:
        model = FloorLayout


#  can import from admin panel
class LayoutAdminConfig(ImportExportModelAdmin):

    resource_class = LayoutResource
    list_display = [
        "name",
        "wall_coordinates",
        "room_coordinates",
    ]


class BuildingAdminConfig(admin.ModelAdmin):
    model = Building
    inlines = [BuildingImageInline, AddressInline, FloorInline]
    list_display = ["building_name", "company", "is_active", "slug", "created_at"]
    list_filter = ["building_name", "company", "is_active"]
    list_editable = ["is_active"]

    prepopulated_fields = {"slug": ("building_name",)}


class FloorAdminConfig(admin.ModelAdmin):
    model = Floor
    list_display = ["title", "level", "created_at", "get_building", "get_layout"]
    inlines = [RoomInline]


class RoomAdminConfig(admin.ModelAdmin):
    model = Room
    list_display = [
        "id",
        "title",
        "capacity",
        "permission_level",
        "created_at",
        "get_floor",
        "get_building",
    ]


class MyEventAdminConfig(admin.ModelAdmin):
    model = MyEvent

    list_display = ["id", "title", "room", "get_floor", "get_building"]


admin.site.register(FloorLayout, LayoutAdminConfig)
admin.site.register(Building, BuildingAdminConfig)
admin.site.register(Floor, FloorAdminConfig)
admin.site.register(Room, RoomAdminConfig)
admin.site.register(MyEvent, MyEventAdminConfig)
