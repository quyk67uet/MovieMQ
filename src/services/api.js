import axios from "axios";
const token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyNmE4Mjc0YWEzOTM3OGJmMTZhN2I5YWFlZTcxZDczNSIsIm5iZiI6MTcyNDQ3MzU3MS4zMzg0OTcsInN1YiI6IjY2Yzk1ZjU4ZWZlNDI3MGRkMDFkNWFiOCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.R1QbWaVCKMaILrfuB0XsAtzfefjfDM70uLzc_dqwQJI";
export default axios.create({
    baseURL: "https://api.themoviedb.org/3",
    headers: {
        Authorization: `Bearer ${token}`
    }
})