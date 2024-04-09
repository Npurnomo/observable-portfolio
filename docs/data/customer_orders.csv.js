import { csvFormat } from "d3-dsv";

// code inspired by Allison Horst

const customers = [];

// Function to generate a random discount percentage between 0 and 30
const getRandomDiscount = () => {
  return Math.floor(Math.random() * 31); // Random number between 0 and 30
};

// Function to generate a random price in Pounds
const getRandomPrice = () => {
  return parseFloat((Math.random() * 1000).toFixed(2)); // Random number between 0 and 1000 with 2 decimal places
};

// Function to generate a random country
const getRandomCountry = () => {
  const countries = ["ENG", "CHI", "IOM", "IRL", "NIR", "SCT", "WAL"];
  return countries[Math.floor(Math.random() * countries.length)]; // Randomly select a state from the array
};

// Function to generate a random device type
const getRandomDeviceType = () => {
  const deviceTypes = ["mobile", "phone", "in store", "other"];
  return deviceTypes[Math.floor(Math.random() * deviceTypes.length)]; // Randomly select a device type from the array
};

// Function to generate a random number of items between 1 and 12
const getRandomNumberOfItems = () => {
  return Math.floor(Math.random() * 12) + 1; // Random number between 1 and 12
};

// Function to generate a random email
const getRandomEmail = (name) => {
  const domains = [
    "gmail.com",
    "yahoo.com",
    "outlook.com",
    "hotmail.com",
    "example.com",
  ];
  const randomDomain = domains[Math.floor(Math.random() * domains.length)]; // Randomly select a domain from the array
  return `${name.replace(/\s+/g, "").toLowerCase()}@${randomDomain}`;
};

// Generate data for 200 customers
for (let i = 1; i <= 500; i++) {
  const id = i;
  const name = `Customer ${i}`;
  const price_pounds = getRandomPrice();
  const discount_pct = getRandomDiscount();
  const total_pounds = price_pounds * (1 - discount_pct / 100); // Calculate discounted price
  const country = getRandomCountry();
  const device_type = getRandomDeviceType();
  const number_of_items = getRandomNumberOfItems();
  const email = getRandomEmail(name);

  // Push customer object to the array
  customers.push({
    id,
    name,
    price_pounds,
    discount_pct,
    total_pounds,
    country,
    device_type,
    number_of_items,
    email,
  });
}

process.stdout.write(csvFormat(customers));