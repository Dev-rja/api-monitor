# API Reliability Monitor — SLA Report

> Last updated: **2026-08-14 04:30 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **77.7%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 69.75% | 3162.6 | 10420.1 | 1000ms | 579/1914 |
| ❌ | `public_apis_list` | 0.0% | 99.63% | 132.5 | 5052.3 | 1500ms | 7/1914 |
| ❌ | `ipapi_check` | 61.49% | 99.95% | 146.9 | 4507.0 | 2500ms | 1/1914 |
| ❌ | `nasa_apod` | 76.91% | 52.93% | 3098.1 | 11152.5 | 2000ms | 901/1914 |
| ⚠️ | `dog_ceo_random` | 96.03% | 97.02% | 519.6 | 10244.1 | 2500ms | 57/1914 |
| ⚠️ | `open_meteo_weather` | 98.96% | 97.86% | 688.6 | 14877.1 | 2000ms | 41/1914 |
| ✅ | `rest_countries` | 99.22% | 98.9% | 285.1 | 10221.5 | 2500ms | 21/1914 |
| ✅ | `useless_fact` | 99.74% | 99.63% | 650.7 | 10229.6 | 2500ms | 7/1914 |
| ✅ | `coingecko_bitcoin` | 99.79% | 99.95% | 96.5 | 4328.4 | 1500ms | 1/1914 |
| ✅ | `catfact_random` | 99.84% | 99.48% | 255.2 | 10080.2 | 3000ms | 10/1914 |
| ✅ | `agify_name` | 99.9% | 99.74% | 392.2 | 16112.2 | 2000ms | 5/1914 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.9% | 194.3 | 3882.8 | 2000ms | 2/1914 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 03:00 | 5004.5 | 50.0% |
| `nasa_apod` | 05:00 | 4561.4 | 63.04% |
| `nasa_apod` | 02:00 | 4524.3 | 66.67% |
| `numbers_trivia` | 10:00 | 4083.3 | 38.89% |
| `nasa_apod` | 03:00 | 4010.5 | 60.53% |
| `numbers_trivia` | 14:00 | 3833.3 | 37.21% |
| `nasa_apod` | 11:00 | 3765.4 | 51.92% |
| `nasa_apod` | 09:00 | 3760.9 | 53.16% |
| `nasa_apod` | 17:00 | 3722.4 | 49.48% |
| `numbers_trivia` | 02:00 | 3607.4 | 33.33% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
