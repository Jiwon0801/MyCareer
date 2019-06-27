 var $temp = $("<input>");
    $("body").append($temp);
    $temp.focus();
    document.execCommand('paste');

    var data =$temp.val();
    $temp.remove();

    try {

        var obj = JSON.parse(data);
        console.log(obj);

        // name
        $('input[ng-model="currentApplicant.specs.basic_information.name.content"]').val(obj.user_name);

        // 임시
        var birth = obj.birth.split('T')[0].split('-');
        var bYear = birth[0];
        var bMonth = birth[1].replace('0','');
        var bDay = birth[2];
        // 년도
        $('select[ng-model="currentApplicant.specs.basic_information.birth.content.year"]').val(bYear).change();
        // 월
        $('select[ng-model="currentApplicant.specs.basic_information.birth.content.month"]').val(bMonth).change();
        // 일
        $('select[ng-model="currentApplicant.specs.basic_information.birth.content.day"]').val(bDay).change();

        // 전화번호
        $('input[ng-model="currentApplicant.specs.basic_information.phone.content"]').val(obj.phone1);
        // 휴대폰 번호
        $('input[ng-model="currentApplicant.specs.basic_information.mobile.content"]').val(obj.phone2);
        // 이메일
        $('input[ng-model="currentApplicant.specs.basic_information.email.content"]').val(obj.email);
        // 주소
        $('input[ng-model="currentApplicant.specs.basic_information.address.content"]').val(obj.addr);

        // 고등학교 시작 년도

        // 고등학교 시작 월

        // 고등학교 종료 년도

        // 고등학교 종료 월

        // 고등학교 명

        // 고등학교 분류

        // 대학교 시작 년도

        // 대학교 시작 월

        // 대학교 종료 년도

        // 대학교 종료 월

        // 대학교명

        // 대학교 분류

        // 대학교 학점

        // 대학교 총점

        // 주전공


        // 자소설 닷컴의 경우, input 창에 focus 되어야 자동 저장됨.
        $('input[ng-model="currentApplicant.specs.basic_information.address.content"]').focus();
    } catch(error) {
        alert('마이커리어닷컴(www.mycareer.com) 에서 [지원하기] 버튼을 눌렀는지 확인해주세요.');
    }
