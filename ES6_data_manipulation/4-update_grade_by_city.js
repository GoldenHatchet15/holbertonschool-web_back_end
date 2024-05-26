const findGrade = (newGrades, studentId) => {
  const gradeObj = newGrades.find((grade) => grade.studentId === studentId);
  return gradeObj ? gradeObj.grade : 'N/A';
};

const updateStudentGradeByCity = (students, city, newGrades) => students
  .filter((student) => student.location === city)
  .map((student) => ({
    ...student,
    grade: findGrade(newGrades, student.id),
  }));

export default updateStudentGradeByCity;
