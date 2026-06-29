# API Reliability Monitor — SLA Report

> Last updated: **2026-06-29 06:55 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.0%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 78.33% | 2361.5 | 10206.7 | 1000ms | 267/1232 |
| ❌ | `public_apis_list` | 0.0% | 99.68% | 125.5 | 4595.4 | 1500ms | 4/1232 |
| ❌ | `nasa_apod` | 74.03% | 49.51% | 3382.0 | 11152.5 | 2000ms | 622/1232 |
| ❌ | `ipapi_check` | 77.27% | 99.92% | 155.7 | 4507.0 | 2500ms | 1/1232 |
| ⚠️ | `rest_countries` | 98.78% | 98.46% | 328.7 | 10221.5 | 2500ms | 19/1232 |
| ⚠️ | `open_meteo_weather` | 98.94% | 97.0% | 713.8 | 14877.1 | 2000ms | 37/1232 |
| ✅ | `useless_fact` | 99.59% | 99.68% | 631.4 | 10229.6 | 2500ms | 4/1232 |
| ✅ | `dog_ceo_random` | 99.59% | 96.59% | 539.7 | 10244.1 | 2500ms | 42/1232 |
| ✅ | `catfact_random` | 99.76% | 99.27% | 259.5 | 10080.2 | 3000ms | 9/1232 |
| ✅ | `coingecko_bitcoin` | 99.76% | 100.0% | 95.5 | 253.3 | 1500ms | 0/1232 |
| ✅ | `agify_name` | 99.92% | 99.68% | 386.8 | 16112.2 | 2000ms | 4/1232 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.84% | 217.6 | 3882.8 | 2000ms | 2/1232 |

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
| `nasa_apod` | 18:00 | 3806.1 | 54.84% |
| `nasa_apod` | 11:00 | 3683.6 | 54.41% |
| `nasa_apod` | 20:00 | 3597.8 | 50.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
