var $temp = $("<input>");
$("body").append($temp);
$temp.focus();
document.execCommand('paste');

var data =$temp.val();
$temp.remove();

try {

    var obj = JSON.parse(data);
    //console.log(obj);

    
    var career_start = obj.career.start.replace('-', '.');
    career_start = career_start.substring(0, 7);

    var career_end = obj.career.career_end.replace('-', '.');
    career_end = career_end.substring(0, 7);
    

    $('#companyName_1').val(obj.career.name);
    $('#careerLocationName_1').val(obj.career.loc);
    $('#orgName_1').val(obj.career.dept);
    $('#gradeName_1').val(obj.career.position);
    $('#careerJobCode_1').val(obj.career.job);
    $('#salary_1').val(obj.career.salary);
    $('#startDate_1').val(career_start);
    $('#endDate_1').val(career_end);

} catch(error) {
    console.log(error)
    alert('마이커리어닷컴(www.mycareer.com) 에서 [지원하기] 버튼을 눌렀는지 확인해주세요.');
}
