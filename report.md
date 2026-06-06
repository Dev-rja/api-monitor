# API Reliability Monitor — SLA Report

> Last updated: **2026-06-06 14:13 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.1%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 73.72% | 2819.7 | 10206.7 | 1000ms | 266/1012 |
| ❌ | `public_apis_list` | 0.0% | 99.6% | 125.8 | 4595.4 | 1500ms | 4/1012 |
| ❌ | `ipapi_check` | 75.69% | 99.9% | 156.8 | 4507.0 | 2500ms | 1/1012 |
| ❌ | `nasa_apod` | 77.47% | 56.42% | 2964.7 | 10565.8 | 2000ms | 441/1012 |
| ⚠️ | `rest_countries` | 98.52% | 98.22% | 355.2 | 10221.5 | 2500ms | 18/1012 |
| ⚠️ | `open_meteo_weather` | 98.91% | 96.94% | 703.3 | 14877.1 | 2000ms | 31/1012 |
| ✅ | `dog_ceo_random` | 99.51% | 95.85% | 578.9 | 10244.1 | 2500ms | 42/1012 |
| ✅ | `catfact_random` | 99.7% | 99.21% | 264.3 | 10080.2 | 3000ms | 8/1012 |
| ✅ | `coingecko_bitcoin` | 99.7% | 100.0% | 96.8 | 253.3 | 1500ms | 0/1012 |
| ✅ | `useless_fact` | 99.8% | 99.6% | 622.4 | 10229.6 | 2500ms | 4/1012 |
| ✅ | `agify_name` | 99.9% | 99.7% | 380.8 | 16112.2 | 2000ms | 3/1012 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.8% | 222.9 | 3882.8 | 2000ms | 2/1012 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 4611.9 | 78.95% |
| `nasa_apod` | 02:00 | 4606.1 | 62.5% |
| `numbers_trivia` | 03:00 | 4408.7 | 42.11% |
| `nasa_apod` | 17:00 | 3959.8 | 50.88% |
| `nasa_apod` | 11:00 | 3824.2 | 49.12% |
| `nasa_apod` | 09:00 | 3820.6 | 50.0% |
| `nasa_apod` | 05:00 | 3766.2 | 62.96% |
| `numbers_trivia` | 05:00 | 3541.5 | 33.33% |
| `numbers_trivia` | 10:00 | 3366.7 | 31.58% |
| `numbers_trivia` | 07:00 | 3340.4 | 31.25% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
