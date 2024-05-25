// 1-get_list_student_ids.js

const getListStudentIds = function (students) {
    if (!Array.isArray(students)) {
      return [];
    }
    return students.map(function (student) {
      return student.id;
    });
};
  
export default getListStudentIds;
  