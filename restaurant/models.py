from django.db import models

class Restaurant(models.Model):
    # restaurant_id = models.BigAutoField(primary_key=True)  # 레스토랑 ID, 자동 생성
    food_category = models.CharField(max_length=30, verbose_name="음식 카테고리")
    local_category = models.CharField(max_length=20, verbose_name="지역")
    title = models.CharField(max_length=30, verbose_name="상호명") #음식카테고리, 로컬카테고리, 상호명은 필수
    imgfile_1 = models.ImageField(null=True, upload_to="", blank=True, verbose_name="이미지1")
    imgfile_2 = models.ImageField(null=True, upload_to="", blank=True, verbose_name="이미지2")
    imgfile_3 = models.ImageField(null=True, upload_to="", blank=True, verbose_name="이미지3") # 이미지 컬럼 추가, 이미지 blank 허용
    image_link = models.CharField(max_length=500, verbose_name="이미지 링크 목록", blank=True, null=True)
    open_day = models.CharField(max_length=10, verbose_name="영업일") #영업일 필수
    close_day = models.CharField(max_length=10, verbose_name="휴일", default='없음', blank=True)
    open_time = models.TimeField(verbose_name="영업 시작 시간", default='00:00')
    close_time = models.TimeField(verbose_name="영업 종료 시간", default='23:59')
    break_time = models.CharField(max_length=20, verbose_name="브레이크 타임", default='', blank=True)
    isParking = models.BooleanField(default=False, verbose_name="주차 가능 여부")
    isValet = models.BooleanField(default=False, verbose_name="발렛파킹 가능 여부")
    isPet = models.BooleanField(default=False, verbose_name="반려동물 동반 가능 여부")
    isPackaging = models.BooleanField(default=False, verbose_name="포장 가능 여부")
    address = models.CharField(max_length=100, verbose_name="주소", blank=True)
    phone = models.CharField(max_length=20, verbose_name="전화번호", blank=True)
    introduction = models.CharField(max_length=200, verbose_name="가게 소개", default='', null=True)
    menu_url = models.URLField(verbose_name="메뉴 URL", default='', null=True)
    latitude = models.FloatField(verbose_name="위치 위도", null=False, default='37.5445023983984')
    longitude = models.FloatField(verbose_name="위치 경도", null=False, default='127.056090471223')
    parking_area = models.CharField(max_length=100, verbose_name="주차장소추천", default='', null=True)
    parking_latitude = models.FloatField(verbose_name="주차장 위도", null=True, default='127.056090471223')
    parkign_longitude = models.FloatField(verbose_name="주차장 경도", null=True, default='127.056090471223')

    def __str__(self):
        return self.title


        #객체를 문자열로 변환할 때 사용되는 메서드입니다.
        #예를 들어, Django의 admin 페이지에서 객체가 표시되는 방식을 정의합니다.
        #이 경우, 객체의 제목(title)을 문자열로 반환합니다.


    def get_image_links(self):
        """
        이미지 링크 목록을 반점으로 구분하여 리스트로 반환합니다.
        """
        if self.image_link:
            return self.image_link.split(',')
        else:
            return []


class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    # menu_id = models.AutoField(primary_key=True)  # 메뉴 ID, 자동 생성
    title1 = models.CharField(max_length=50, verbose_name="메인메뉴1 이름", default='', null=True)
    price1 = models.CharField(max_length=20, verbose_name="메인메뉴1 가격", default='', null=True)  # 기본값 추가
    title2 = models.CharField(max_length=50, verbose_name="메인메뉴2 이름", default='', null=True)
    price2 = models.CharField(max_length=20, verbose_name="메인메뉴2 가격", default='',  null=True)  # 기본값 추가