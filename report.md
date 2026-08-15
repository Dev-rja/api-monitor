# API Reliability Monitor — SLA Report

> Last updated: **2026-08-15 20:39 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **77.6%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 67.53% | 3383.1 | 10420.1 | 1000ms | 642/1977 |
| ❌ | `public_apis_list` | 0.0% | 99.54% | 136.2 | 5075.4 | 1500ms | 9/1977 |
| ❌ | `ipapi_check` | 59.69% | 99.95% | 146.3 | 4507.0 | 2500ms | 1/1977 |
| ❌ | `nasa_apod` | 77.54% | 53.57% | 3043.3 | 11152.5 | 2000ms | 918/1977 |
| ⚠️ | `dog_ceo_random` | 96.16% | 97.07% | 513.8 | 10244.1 | 2500ms | 58/1977 |
| ⚠️ | `open_meteo_weather` | 98.89% | 97.82% | 693.1 | 14877.1 | 2000ms | 43/1977 |
| ✅ | `rest_countries` | 99.24% | 98.94% | 282.1 | 10221.5 | 2500ms | 21/1977 |
| ✅ | `useless_fact` | 99.75% | 99.65% | 650.8 | 10229.6 | 2500ms | 7/1977 |
| ✅ | `catfact_random` | 99.8% | 99.44% | 260.0 | 10080.2 | 3000ms | 11/1977 |
| ✅ | `coingecko_bitcoin` | 99.8% | 99.95% | 96.1 | 4328.4 | 1500ms | 1/1977 |
| ✅ | `agify_name` | 99.9% | 99.75% | 392.3 | 16112.2 | 2000ms | 5/1977 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.9% | 192.8 | 3882.8 | 2000ms | 2/1977 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 5135.5 | 51.28% |
| `nasa_apod` | 05:00 | 4347.0 | 61.22% |
| `numbers_trivia` | 10:00 | 4323.2 | 41.33% |
| `nasa_apod` | 02:00 | 4198.8 | 61.54% |
| `numbers_trivia` | 02:00 | 4103.1 | 38.46% |
| `numbers_trivia` | 14:00 | 4043.7 | 39.33% |
| `nasa_apod` | 03:00 | 3922.3 | 58.97% |
| `numbers_trivia` | 05:00 | 3858.6 | 36.73% |
| `nasa_apod` | 09:00 | 3738.9 | 53.66% |
| `nasa_apod` | 17:00 | 3693.1 | 48.51% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
