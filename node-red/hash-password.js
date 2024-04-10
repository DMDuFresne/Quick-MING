const bcrypt = require('bcryptjs');
const password = process.argv[2]; // Password from command line argument

bcrypt.hash(password, 8, function(err, hash) {
    if (err) {
        console.error('Error hashing password:', err);
        process.exit(1);
    } else {
        console.log(hash); // Output the hashed password
    }
});