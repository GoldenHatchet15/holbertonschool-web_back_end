import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

function handleProfileSignup(firstName, lastName, fileName) {
  const promises = [
    signUpUser(firstName, lastName),
    uploadPhoto(fileName)
  ];

  return Promise.allSettled(promises).then((results) => {
    return results.map((result) => {
      if (result.status === 'fulfilled') {
        return { status: 'fulfilled', value: result.value };
      } else {
        return { status: 'rejected', value: result.reason };
      }
    });
  });
}

export default handleProfileSignup;
