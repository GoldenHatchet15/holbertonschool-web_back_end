function updateStudentGradeByCity(students, city, newGrades) {
  // Check if students is an array
  if (!Array.isArray(students)) {
    return [];
  }

  // Check if city is a string
  if (typeof city !== 'string') {
    return [];
  }

  // Check if newGrades is an array
  if (!Array.isArray(newGrades)) {
    return [];
  }

  return students
    .filter((student) => student.location === city)
    .map((student) => {
      const gradeObj = newGrades.find((grade) => grade.studentId === student.id);
      return { ...student, grade: gradeObj ? gradeObj.grade : 'N/A' };
    });
}

export default updateStudentGradeByCity;
