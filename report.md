# API Reliability Monitor — SLA Report

> Last updated: **2026-06-28 14:51 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.0%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 78.17% | 2377.3 | 10206.7 | 1000ms | 267/1223 |
| ❌ | `public_apis_list` | 0.0% | 99.67% | 125.4 | 4595.4 | 1500ms | 4/1223 |
| ❌ | `nasa_apod` | 74.08% | 49.8% | 3370.6 | 11152.5 | 2000ms | 614/1223 |
| ❌ | `ipapi_check` | 77.11% | 99.92% | 155.6 | 4507.0 | 2500ms | 1/1223 |
| ⚠️ | `rest_countries` | 98.77% | 98.45% | 329.6 | 10221.5 | 2500ms | 19/1223 |
| ⚠️ | `open_meteo_weather` | 98.94% | 96.97% | 714.8 | 14877.1 | 2000ms | 37/1223 |
| ✅ | `useless_fact` | 99.59% | 99.67% | 631.7 | 10229.6 | 2500ms | 4/1223 |
| ✅ | `dog_ceo_random` | 99.59% | 96.57% | 541.0 | 10244.1 | 2500ms | 42/1223 |
| ✅ | `catfact_random` | 99.75% | 99.26% | 259.1 | 10080.2 | 3000ms | 9/1223 |
| ✅ | `coingecko_bitcoin` | 99.75% | 100.0% | 95.5 | 253.3 | 1500ms | 0/1223 |
| ✅ | `agify_name` | 99.92% | 99.67% | 386.7 | 16112.2 | 2000ms | 4/1223 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.84% | 217.5 | 3882.8 | 2000ms | 2/1223 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 02:00 | 5333.5 | 66.67% |
| `nasa_apod` | 03:00 | 4897.3 | 80.0% |
| `nasa_apod` | 05:00 | 4594.8 | 67.65% |
| `nasa_apod` | 09:00 | 4467.2 | 56.6% |
| `nasa_apod` | 01:00 | 4246.8 | 62.5% |
| `nasa_apod` | 17:00 | 4222.4 | 56.06% |
| `numbers_trivia` | 03:00 | 4200.6 | 40.0% |
| `nasa_apod` | 18:00 | 3824.0 | 54.1% |
| `nasa_apod` | 11:00 | 3683.6 | 54.41% |
| `nasa_apod` | 20:00 | 3610.8 | 49.37% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
