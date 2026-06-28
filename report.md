# API Reliability Monitor — SLA Report

> Last updated: **2026-06-28 21:15 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.0%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 78.26% | 2368.4 | 10206.7 | 1000ms | 267/1228 |
| ❌ | `public_apis_list` | 0.0% | 99.67% | 125.5 | 4595.4 | 1500ms | 4/1228 |
| ❌ | `nasa_apod` | 74.1% | 49.67% | 3372.2 | 11152.5 | 2000ms | 618/1228 |
| ❌ | `ipapi_check` | 77.2% | 99.92% | 155.7 | 4507.0 | 2500ms | 1/1228 |
| ⚠️ | `rest_countries` | 98.78% | 98.45% | 329.3 | 10221.5 | 2500ms | 19/1228 |
| ⚠️ | `open_meteo_weather` | 98.94% | 96.99% | 714.3 | 14877.1 | 2000ms | 37/1228 |
| ✅ | `useless_fact` | 99.59% | 99.67% | 631.6 | 10229.6 | 2500ms | 4/1228 |
| ✅ | `dog_ceo_random` | 99.59% | 96.58% | 540.3 | 10244.1 | 2500ms | 42/1228 |
| ✅ | `catfact_random` | 99.76% | 99.27% | 259.5 | 10080.2 | 3000ms | 9/1228 |
| ✅ | `coingecko_bitcoin` | 99.76% | 100.0% | 95.6 | 253.3 | 1500ms | 0/1228 |
| ✅ | `agify_name` | 99.92% | 99.67% | 386.8 | 16112.2 | 2000ms | 4/1228 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.84% | 217.5 | 3882.8 | 2000ms | 2/1228 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 02:00 | 5333.5 | 66.67% |
| `nasa_apod` | 03:00 | 4897.3 | 80.0% |
| `nasa_apod` | 05:00 | 4594.8 | 67.65% |
| `nasa_apod` | 09:00 | 4467.2 | 56.6% |
| `nasa_apod` | 01:00 | 4246.8 | 62.5% |
| `numbers_trivia` | 03:00 | 4200.6 | 40.0% |
| `nasa_apod` | 17:00 | 4168.0 | 55.22% |
| `nasa_apod` | 18:00 | 3806.1 | 54.84% |
| `nasa_apod` | 11:00 | 3683.6 | 54.41% |
| `nasa_apod` | 20:00 | 3597.8 | 50.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
