# API Reliability Monitor — SLA Report

> Last updated: **2026-06-29 21:49 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.0%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 78.42% | 2352.8 | 10206.7 | 1000ms | 267/1237 |
| ❌ | `public_apis_list` | 0.0% | 99.68% | 125.7 | 4595.4 | 1500ms | 4/1237 |
| ❌ | `nasa_apod` | 73.89% | 49.47% | 3394.0 | 11152.5 | 2000ms | 625/1237 |
| ❌ | `ipapi_check` | 77.28% | 99.92% | 155.6 | 4507.0 | 2500ms | 1/1237 |
| ⚠️ | `rest_countries` | 98.79% | 98.46% | 328.0 | 10221.5 | 2500ms | 19/1237 |
| ⚠️ | `open_meteo_weather` | 98.95% | 97.01% | 713.1 | 14877.1 | 2000ms | 37/1237 |
| ✅ | `useless_fact` | 99.6% | 99.68% | 631.4 | 10229.6 | 2500ms | 4/1237 |
| ✅ | `dog_ceo_random` | 99.6% | 96.6% | 538.9 | 10244.1 | 2500ms | 42/1237 |
| ✅ | `catfact_random` | 99.76% | 99.27% | 258.9 | 10080.2 | 3000ms | 9/1237 |
| ✅ | `coingecko_bitcoin` | 99.76% | 100.0% | 95.4 | 253.3 | 1500ms | 0/1237 |
| ✅ | `agify_name` | 99.92% | 99.68% | 386.8 | 16112.2 | 2000ms | 4/1237 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.84% | 217.4 | 3882.8 | 2000ms | 2/1237 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 02:00 | 5333.5 | 66.67% |
| `nasa_apod` | 03:00 | 4897.3 | 80.0% |
| `nasa_apod` | 05:00 | 4594.8 | 67.65% |
| `nasa_apod` | 09:00 | 4467.2 | 56.6% |
| `numbers_trivia` | 03:00 | 4200.6 | 40.0% |
| `nasa_apod` | 01:00 | 4192.5 | 63.64% |
| `nasa_apod` | 17:00 | 4168.0 | 55.22% |
| `nasa_apod` | 18:00 | 3910.9 | 55.56% |
| `nasa_apod` | 11:00 | 3683.6 | 54.41% |
| `nasa_apod` | 20:00 | 3681.4 | 50.62% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
