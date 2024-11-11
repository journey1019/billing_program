from django.contrib import admin
from .models import Pplan

@admin.register(Pplan)
class PplanAdmin(admin.ModelAdmin):
    list_display = ('ppid', 'basic_fee', 'subscription_fee', 'free_byte', 'surcharge_unit', 'each_surcharge_fee', 'apply_company', 'remarks', 'note')
    search_fields = ('ppid', 'basic_fee', 'subscription_fee', 'free_byte', 'surcharge_unit', 'each_surcharge_fee', 'apply_company', 'remarks', 'note')

    # 필터 사이드바에 표시할 필드
    list_filter = ('apply_company',)

    # 읽기 전용 필드 (수정 불가)
    readonly_fields = ('ppid',)

    # 인라인 액션
    actions = ['reset_subscription_fee']

    def reset_subscription_fee(self, request, queryset):
        # 선택된 항목의 subscription_fee를 0으로 초기화하는 예시
        queryset.update(subscription_fee=0)
        self.message_user(request, "선택된 플랜의 구독 요금이 초기화되었습니다.")
    reset_subscription_fee.short_description = "구독 요금 초기화"

    # 삭제 확인 메시지
    def delete_model(self, request, obj):
        obj.delete()
        self.message_user(request, f"{obj.ppid}가 성공적으로 삭제되었습니다.")

    # 개별 객체 삭제 허용 (일반적으로 필요 없음)
    def has_delete_permission(self, request, obj=None):
        return True  # False로 설정하면 삭제 버튼이 비활성화됨