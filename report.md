# API Reliability Monitor — SLA Report

> Last updated: **2026-08-15 10:13 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **77.6%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 68.36% | 3300.7 | 10420.1 | 1000ms | 618/1953 |
| ❌ | `public_apis_list` | 0.0% | 99.54% | 136.1 | 5075.4 | 1500ms | 9/1953 |
| ❌ | `ipapi_check` | 60.32% | 99.95% | 146.4 | 4507.0 | 2500ms | 1/1953 |
| ❌ | `nasa_apod` | 77.32% | 53.25% | 3065.5 | 11152.5 | 2000ms | 913/1953 |
| ⚠️ | `dog_ceo_random` | 96.11% | 97.03% | 516.5 | 10244.1 | 2500ms | 58/1953 |
| ⚠️ | `open_meteo_weather` | 98.87% | 97.85% | 691.6 | 14877.1 | 2000ms | 42/1953 |
| ✅ | `rest_countries` | 99.23% | 98.92% | 283.4 | 10221.5 | 2500ms | 21/1953 |
| ✅ | `useless_fact` | 99.74% | 99.64% | 650.9 | 10229.6 | 2500ms | 7/1953 |
| ✅ | `catfact_random` | 99.8% | 99.44% | 259.8 | 10080.2 | 3000ms | 11/1953 |
| ✅ | `coingecko_bitcoin` | 99.8% | 99.95% | 96.3 | 4328.4 | 1500ms | 1/1953 |
| ✅ | `agify_name` | 99.9% | 99.74% | 392.7 | 16112.2 | 2000ms | 5/1953 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.9% | 193.4 | 3882.8 | 2000ms | 2/1953 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 5135.5 | 51.28% |
| `nasa_apod` | 05:00 | 4347.0 | 61.22% |
| `numbers_trivia` | 10:00 | 4244.5 | 40.54% |
| `nasa_apod` | 02:00 | 4198.8 | 61.54% |
| `numbers_trivia` | 02:00 | 4103.1 | 38.46% |
| `nasa_apod` | 03:00 | 3922.3 | 58.97% |
| `numbers_trivia` | 14:00 | 3905.2 | 37.93% |
| `numbers_trivia` | 05:00 | 3858.6 | 36.73% |
| `nasa_apod` | 09:00 | 3738.9 | 53.66% |
| `nasa_apod` | 11:00 | 3735.5 | 51.43% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
