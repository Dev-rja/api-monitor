# API Reliability Monitor — SLA Report

> Last updated: **2026-08-15 13:37 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **77.6%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 68.11% | 3325.0 | 10420.1 | 1000ms | 625/1960 |
| ❌ | `public_apis_list` | 0.0% | 99.54% | 136.1 | 5075.4 | 1500ms | 9/1960 |
| ❌ | `ipapi_check` | 60.15% | 99.95% | 146.3 | 4507.0 | 2500ms | 1/1960 |
| ❌ | `nasa_apod` | 77.4% | 53.32% | 3058.1 | 11152.5 | 2000ms | 915/1960 |
| ⚠️ | `dog_ceo_random` | 96.12% | 97.04% | 515.5 | 10244.1 | 2500ms | 58/1960 |
| ⚠️ | `open_meteo_weather` | 98.88% | 97.81% | 693.6 | 14877.1 | 2000ms | 43/1960 |
| ✅ | `rest_countries` | 99.23% | 98.93% | 283.0 | 10221.5 | 2500ms | 21/1960 |
| ✅ | `useless_fact` | 99.74% | 99.64% | 651.0 | 10229.6 | 2500ms | 7/1960 |
| ✅ | `catfact_random` | 99.8% | 99.44% | 259.7 | 10080.2 | 3000ms | 11/1960 |
| ✅ | `coingecko_bitcoin` | 99.8% | 99.95% | 96.3 | 4328.4 | 1500ms | 1/1960 |
| ✅ | `agify_name` | 99.9% | 99.74% | 392.7 | 16112.2 | 2000ms | 5/1960 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.9% | 193.2 | 3882.8 | 2000ms | 2/1960 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 5135.5 | 51.28% |
| `nasa_apod` | 05:00 | 4347.0 | 61.22% |
| `numbers_trivia` | 10:00 | 4323.2 | 41.33% |
| `nasa_apod` | 02:00 | 4198.8 | 61.54% |
| `numbers_trivia` | 02:00 | 4103.1 | 38.46% |
| `nasa_apod` | 03:00 | 3922.3 | 58.97% |
| `numbers_trivia` | 14:00 | 3905.2 | 37.93% |
| `numbers_trivia` | 05:00 | 3858.6 | 36.73% |
| `nasa_apod` | 09:00 | 3738.9 | 53.66% |
| `nasa_apod` | 17:00 | 3658.9 | 48.48% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
