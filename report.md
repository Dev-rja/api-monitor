# API Reliability Monitor — SLA Report

> Last updated: **2026-08-01 22:04 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **78.3%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 78.7% | 2282.5 | 10420.1 | 1000ms | 358/1681 |
| ❌ | `public_apis_list` | 0.0% | 99.7% | 129.3 | 5052.3 | 1500ms | 5/1681 |
| ❌ | `ipapi_check` | 68.59% | 99.94% | 149.9 | 4507.0 | 2500ms | 1/1681 |
| ❌ | `nasa_apod` | 78.11% | 55.09% | 2952.1 | 11152.5 | 2000ms | 755/1681 |
| ⚠️ | `dog_ceo_random` | 95.48% | 96.61% | 543.5 | 10244.1 | 2500ms | 57/1681 |
| ⚠️ | `open_meteo_weather` | 98.87% | 97.56% | 700.4 | 14877.1 | 2000ms | 41/1681 |
| ✅ | `rest_countries` | 99.11% | 98.75% | 295.8 | 10221.5 | 2500ms | 21/1681 |
| ✅ | `useless_fact` | 99.7% | 99.7% | 643.6 | 10229.6 | 2500ms | 5/1681 |
| ✅ | `catfact_random` | 99.82% | 99.46% | 258.2 | 10080.2 | 3000ms | 9/1681 |
| ✅ | `coingecko_bitcoin` | 99.82% | 99.94% | 96.8 | 4328.4 | 1500ms | 1/1681 |
| ✅ | `agify_name` | 99.88% | 99.76% | 389.4 | 16112.2 | 2000ms | 4/1681 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.88% | 199.6 | 3882.8 | 2000ms | 2/1681 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 02:00 | 5333.5 | 66.67% |
| `nasa_apod` | 05:00 | 4220.5 | 60.0% |
| `numbers_trivia` | 03:00 | 4217.1 | 40.0% |
| `nasa_apod` | 03:00 | 3899.0 | 63.33% |
| `nasa_apod` | 09:00 | 3718.2 | 48.57% |
| `nasa_apod` | 17:00 | 3549.1 | 48.84% |
| `nasa_apod` | 12:00 | 3389.4 | 51.39% |
| `nasa_apod` | 01:00 | 3257.3 | 46.15% |
| `nasa_apod` | 11:00 | 3243.2 | 47.83% |
| `nasa_apod` | 18:00 | 3183.4 | 46.24% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
