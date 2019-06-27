
    var dialogs = [];
    const csrf = $('input[name="csrfmiddlewaretoken"]').first().val();
    
    $(function () {
        $('[data-toggle="tooltip"]').tooltip();


        //$( "#settingModal" ).modal(); 모달 자동 열기..

        // dialog 생성
        $(".timeline-content").click(function (e) {
            var isOpen = false;
            var id = $(this).data('id');
            var item = $(this).data('item');
            var pk = $(this).data('pk');

            $.each( dialogs, function( key, obj ) {
                if(obj.config.id == id) {
                    isOpen = true;
                    return false;
                }
            });

            if(isOpen) {
                alert('이미 열려있습니다.');
            }
            else {
                var content='';

                $.ajax({
                    type: "POST",
                    url: '/detail/'+item+'/'+pk+'/',
                    data: { 'csrfmiddlewaretoken' : csrf },
                    async:false,
                    dataType: "text",
                    success: function(res){
                        content = res;
                        // content ='<div class="kt-widget-5__item kt-widget-5__item--info"><div class="kt-widget-5__item-info"><div class="kt-widget-5__item-datetime">학교명</div><a href="#" class="kt-widget-5__item-title">멀캠대학교</a></div></div>';                        
                    },
                    error: function(request, status, error){ // 통신 실패시 - 로그인 페이지 리다이렉트
                        alert('전체 삭제에 실패했습니다.');
                        console.log(error);
                    }
                });
            //     var httt = `<div class="kt-widget-5__item-info">
            //     <div class="kt-widget-5__item-datetime">
            //         학교명
            //     </div>
            //     <a href="#" class="kt-widget-5__item-title">
            //         멀캠대학교
            //     </a>
            // </div>`;
                var dialog = $.dialog({
		        content : `<div class="" style="width:400px;max-height:500px;"><div class="kt-widget-5">
                    ${content}
                </div></div>`,
		        hasMask : false,
		        id : id,
		        hotKeys : false,
                width:'auto',
                resize: 'auto',
                height: 'auto',
		        autoFocus   : true,
		        hasTitle : true,
		        top : (e.pageY+30)-$(document).scrollTop(),
		        left : e.pageX+30,
		        onClose : function(){
                    var idx = -1;
		            $.each( dialogs, function( key, obj ) {
		                if (obj.config.id == id) {
		                    idx = key;
		                    return false;
		                }
                    });

                    if (idx > -1) {
                        dialogs.splice(idx, 1);
                    }
                }

	            });
                dialog.open();
                dialogs.push(dialog);
            }
        });

        $("#btnAddMajor").click(function ()  {
			var html = `<div class="col-md-3 pb-0">
				<select name="" id="" class="form-control">
					<option class="text-dark" value="">전공구분 선택</option>
					<option class="text-dark" value="">전공</option>
					<option class="text-dark" value="">부전공</option>
					<option class="text-dark" value="">복수전공</option>
				</select>
			</div>
			<div class="col-md-3 pb-0">
				<select name="" class="form-control">
					<option class="dark" value="">전공계열 선택</option>
					<option class="text-dark" value="">어문학</option>
					<option class="text-dark" value="">영어/영문</option>
					<option class="text-dark" value="">중어/중문</option>
				</select>
			</div>
			<div class="col-md-4 pb-0">
				<div class="form-group">
					<input type="text" class="form-control" placeholder="전공학과 입력">
				</div>
			</div>
			<div class="col-auto pb-0">
				<div class="form-group">
					<button id="btnDelMajor" type="button" class="btn btn-outline-dark ml-1">삭제</button>
				</div>
			</div>`;

            $("#wrapSubMajor").html(html);
            $("#btnAddMajor").hide();
            $('#btnDelMajor').on('click', function() {
                $("#btnAddMajor").show();
                $("#wrapSubMajor").empty();
            });
        });

        $(".edu-title").click(function () {
            $("#"+$(this).data('section')).collapse("toggle");
        });
    
    
       
    // 성적 모두 지우기
    $(".btnDelAllSubject").click(function () {
        if(confirm("입력하신 성적을 모두 지우시겠습니까?")){
            var section = $(this).data('section');
            $("#"+section).find('tbody').empty();

            $.ajax({
                type: "POST",
                url: '/grade/delete/',
                data: { 'csrfmiddlewaretoken' : csrf },
                dataType: "json",
                success: function(res){
                    if(res.data == 200) {
                        alert('성공적으로 완료했습니다.');
                    }
                    else {
                        alert('전체 삭제에 실패했습니다.');
                    }
                },
                error: function(request, status, error){ // 통신 실패시 - 로그인 페이지 리다이렉트
                    alert('전체 삭제에 실패했습니다.');
                    console.log(error);
                }
            });

        }
    });

    // 전공 추가하기
    $(".btnAddSubject").click(function () {
        var section = $(this).data('section');

        var idx = $("#"+section).find('tbody').find('tr').length +1;

        var html = `<tr>
            <td  class="text-center">${idx}</td>
            <td><select name="year" class="form-control">
                                    <option class="text-dark" value="2019">2019</option>
                                    <option class="text-dark" value="2018">2018</option>
                                    <option class="text-dark" value="2017">2017</option>
                                </select></td>
            <td><select name="semester" class="form-control">
                                    <option class="text-dark" value="1">1</option>
                                    <option class="text-dark" value="2">2</option>
                                    <option class="text-dark" value="여름계절">여름계절</option>
                                    <option class="text-dark" value="겨울계절">겨울계절</option>
                                </select></td>
            <td><select name="major_yn" class="form-control">
                                    <option class="text-dark" value="전공">전공</option>
                                    <option class="text-dark" value="전공필수">전공필수</option>
                                    <option class="text-dark" value="교양필수">교양필수</option>
                                    <option class="text-dark" value="교양기타">교양기타</option>
                                </select></td>
            <td><select name="credit" class="form-control">
                                    <option class="text-dark" value="0">0</option>
                                    <option class="text-dark" value="1">1</option>
                                    <option class="text-dark" value="2">2</option>
                                    <option class="text-dark" value="3">3</option>
                                </select></td>
            <td><input type="text" name="name" class="form-control"></td>
            <td><select name="grade" class="form-control">
                                    <option class="text-dark" value="A+">A+</option>
                                    <option class="text-dark" value="A0">A0</option>
                                    <option class="text-dark" value="A-">A-</option>
                                    <option class="text-dark" value="B+">B+</option>
                                    <option class="text-dark" value="B0">B0</option>
                                    <option class="text-dark" value="B-">B-</option>
                                    <option class="text-dark" value="C+">C+</option>
                                    <option class="text-dark" value="C0">C0</option>
                                    <option class="text-dark" value="C-">C-</option>
                                    <option class="text-dark" value="D+">D+</option>
                                    <option class="text-dark" value="D0">D0</option>
                                    <option class="text-dark" value="D-">D-</option>
                                    <option class="text-dark" value="F">F</option>
                                    <option class="text-dark" value="PASS">PASS</option>
                                    <option class="text-dark" value="FAIL">FAIL</option>
                                </select></td>
            <td><select name="re_join" class="form-control">
                                    <option class="text-dark" value="Y">Y</option>
                                    <option class="text-dark" value="N">N</option>
                                </select></td>
            <td>
                <button type="button" onclick="deleteSubject(this)" class="btn btn-link btn-sm text-muted">삭제</button> / 
                <button type="button" onclick="submitSubject(this)" class="btn btn-link btn-sm text-muted">확인</button>
            </td>
        </tr>`;

        $("#"+section).find('table>tbody').append(html);
        $(this)[0].scrollIntoView(false);
    });

    });
    // end of function.

    // 성적 추가하기
    function submitSubject(element) {
        var $form = $('<form action="/grade/create/"></form>');
        var $row = $(element).parent().parent();
        var $name = $row.find('input');

        $form.append('<input type="hideen" name="'+$name.attr('name')+'" value="'+$name.val()+'">');
        $form.append('<input type="hideen" name="csrfmiddlewaretoken" value="'+csrf+'">');

        $row.find('select').each(function (key,obj) {
            $form.append('<input type="hideen" name="'+$(obj).attr('name')+'" value="'+$(obj).val()+'">');
        });
        
        $.ajax({
            type: "POST",
            url: $form.attr('action'),
            data: $form.serialize(),
            dataType: "json",
            success: function(res){
                if(res.data == 200) {
                    alert('정상적으로 추가했습니다.');
                }
                else {
                    alert('추가에 실패했습니다. 잠시 후 다시 시도해주세요.');
                }
            },
            error: function(request, status, error){ // 통신 실패시 - 로그인 페이지 리다이렉트
                alert('추가에 실패했습니다. 잠시 후 다시 시도해주세요.');
                console.log(error);
            }
        });
        $form = null;
    }

    // 성적 수정하기
    function updateSubject(element) {
        var pk = $(element).data('pk');
        var $form = $('<form action="/grade/'+pk+'/update/"></form>');
        var $row = $(element).parent().parent();
        var $name = $row.find('input');

        $form.append('<input type="hideen" name="'+$name.attr('name')+'" value="'+$name.val()+'">');
        $form.append('<input type="hideen" name="csrfmiddlewaretoken" value="'+csrf+'">');

        $row.find('select').each(function (key,obj) {
            $form.append('<input type="hideen" name="'+$(obj).attr('name')+'" value="'+$(obj).val()+'">');
        });

        $.ajax({
            type: "POST",
            url: $form.attr('action'),
            data: $form.serialize(),
            dataType: "json",
            success: function(res){
                if(res.data == 200) {
                    alert('정상적으로 수정했습니다.');
                }
                else {
                    alert('수정에 실패했습니다. 잠시 후 다시 시도해주세요.');
                }
            },
            error: function(request, status, error){ // 통신 실패시 - 로그인 페이지 리다이렉트
                alert('수정에 실패했습니다. 잠시 후 다시 시도해주세요.');
                console.log(error);
            }
        });
        $form = null;
    }

    // 성적 삭제하기
    function deleteSubject(element) {
        if(confirm('과목을 삭제하시겠습니까?')) {
            var rows = $(element).closest('table>tbody');
            var pk = $(element).data('pk');

            $(element).parent().parent().remove();

            rows.find('tr').each(function( idx, row ) {
                $(row).find('td:first-child').html(idx+1);
            });
            
            if(pk != undefined) {
                $.ajax({
                    type: "POST",
                    url: '/grade/'+pk+'/delete/',
                    data: {'csrfmiddlewaretoken': csrf},
                    dataType: "json",
                    success: function(res){
                        alert('과목을 삭제했습니다.');
                    },
                    error: function(request, status, error){ // 통신 실패시 - 로그인 페이지 리다이렉트
                        console.log(error);
                    }
                });
            }
        }
    }


    function toggleSide(element) {
        if($(element).data('open')) {
            document.getElementById("mySidenav").style.width = "0";
            $(element).data('open', false);
        }
        else {
            document.getElementById("mySidenav").style.width = "330px";
            $(element).data('open', true);
        }
    }

    function closeNav() {
        document.getElementById("mySidenav").style.width = "0";
    }



    function closeAllDialog() {
        alert('아직 지원하지 않는 기능입니다.');
        return false;

        try {
            $.each( dialogs, function( key, obj ) {
            obj.close();
        });
        }
        catch(error) {
        $.each( dialogs, function( key, obj ) {
            obj.close();
        });
        }

    }
