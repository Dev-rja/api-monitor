# API Reliability Monitor — SLA Report

> Last updated: **2026-08-15 11:29 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **77.6%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 68.25% | 3311.2 | 10420.1 | 1000ms | 621/1956 |
| ❌ | `public_apis_list` | 0.0% | 99.54% | 136.2 | 5075.4 | 1500ms | 9/1956 |
| ❌ | `ipapi_check` | 60.28% | 99.95% | 146.4 | 4507.0 | 2500ms | 1/1956 |
| ❌ | `nasa_apod` | 77.35% | 53.27% | 3062.3 | 11152.5 | 2000ms | 914/1956 |
| ⚠️ | `dog_ceo_random` | 96.11% | 97.03% | 516.1 | 10244.1 | 2500ms | 58/1956 |
| ⚠️ | `open_meteo_weather` | 98.88% | 97.85% | 691.8 | 14877.1 | 2000ms | 42/1956 |
| ✅ | `rest_countries` | 99.23% | 98.93% | 283.2 | 10221.5 | 2500ms | 21/1956 |
| ✅ | `useless_fact` | 99.74% | 99.64% | 651.1 | 10229.6 | 2500ms | 7/1956 |
| ✅ | `catfact_random` | 99.8% | 99.44% | 259.7 | 10080.2 | 3000ms | 11/1956 |
| ✅ | `coingecko_bitcoin` | 99.8% | 99.95% | 96.3 | 4328.4 | 1500ms | 1/1956 |
| ✅ | `agify_name` | 99.9% | 99.74% | 392.8 | 16112.2 | 2000ms | 5/1956 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.9% | 193.3 | 3882.8 | 2000ms | 2/1956 |

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
| `nasa_apod` | 11:00 | 3670.8 | 50.47% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
