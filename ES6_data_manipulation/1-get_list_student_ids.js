function getListStudentIds(students) {
    if (!Array.isArray(students)) {
      return [];
    }
    return students.map(function (student) {
      return student.id;
    });
  }
  
  export default getListStudentIds;
  