# API Reliability Monitor — SLA Report

> Last updated: **2026-08-15 17:24 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **77.6%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 67.8% | 3355.9 | 10420.1 | 1000ms | 634/1969 |
| ❌ | `public_apis_list` | 0.0% | 99.54% | 136.2 | 5075.4 | 1500ms | 9/1969 |
| ❌ | `ipapi_check` | 59.88% | 99.95% | 146.4 | 4507.0 | 2500ms | 1/1969 |
| ❌ | `nasa_apod` | 77.5% | 53.53% | 3046.2 | 11152.5 | 2000ms | 915/1969 |
| ⚠️ | `dog_ceo_random` | 96.14% | 97.05% | 514.4 | 10244.1 | 2500ms | 58/1969 |
| ⚠️ | `open_meteo_weather` | 98.88% | 97.82% | 693.1 | 14877.1 | 2000ms | 43/1969 |
| ✅ | `rest_countries` | 99.24% | 98.93% | 282.5 | 10221.5 | 2500ms | 21/1969 |
| ✅ | `useless_fact` | 99.75% | 99.64% | 650.9 | 10229.6 | 2500ms | 7/1969 |
| ✅ | `catfact_random` | 99.8% | 99.44% | 259.2 | 10080.2 | 3000ms | 11/1969 |
| ✅ | `coingecko_bitcoin` | 99.8% | 99.95% | 96.2 | 4328.4 | 1500ms | 1/1969 |
| ✅ | `agify_name` | 99.9% | 99.75% | 392.3 | 16112.2 | 2000ms | 5/1969 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.9% | 193.0 | 3882.8 | 2000ms | 2/1969 |

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
| `nasa_apod` | 11:00 | 3640.4 | 50.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
