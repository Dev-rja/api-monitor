# API Reliability Monitor — SLA Report

> Last updated: **2026-06-17 13:55 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.0%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 76.08% | 2585.1 | 10206.7 | 1000ms | 266/1112 |
| ❌ | `public_apis_list` | 0.0% | 99.64% | 125.4 | 4595.4 | 1500ms | 4/1112 |
| ❌ | `nasa_apod` | 75.27% | 52.97% | 3201.1 | 11152.5 | 2000ms | 523/1112 |
| ❌ | `ipapi_check` | 76.17% | 99.91% | 156.1 | 4507.0 | 2500ms | 1/1112 |
| ⚠️ | `rest_countries` | 98.65% | 98.38% | 339.8 | 10221.5 | 2500ms | 18/1112 |
| ⚠️ | `open_meteo_weather` | 98.92% | 96.76% | 718.2 | 14877.1 | 2000ms | 36/1112 |
| ✅ | `dog_ceo_random` | 99.55% | 96.22% | 559.6 | 10244.1 | 2500ms | 42/1112 |
| ✅ | `catfact_random` | 99.73% | 99.19% | 263.2 | 10080.2 | 3000ms | 9/1112 |
| ✅ | `coingecko_bitcoin` | 99.73% | 100.0% | 96.3 | 253.3 | 1500ms | 0/1112 |
| ✅ | `useless_fact` | 99.82% | 99.64% | 626.9 | 10229.6 | 2500ms | 4/1112 |
| ✅ | `agify_name` | 99.91% | 99.73% | 378.3 | 16112.2 | 2000ms | 3/1112 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.82% | 218.9 | 3882.8 | 2000ms | 2/1112 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 02:00 | 5333.5 | 66.67% |
| `nasa_apod` | 03:00 | 4611.9 | 78.95% |
| `nasa_apod` | 05:00 | 4415.7 | 66.67% |
| `numbers_trivia` | 03:00 | 4408.7 | 42.11% |
| `nasa_apod` | 17:00 | 4096.3 | 54.84% |
| `nasa_apod` | 09:00 | 4014.2 | 52.08% |
| `nasa_apod` | 11:00 | 3861.7 | 50.0% |
| `nasa_apod` | 01:00 | 3752.8 | 53.85% |
| `nasa_apod` | 18:00 | 3616.1 | 52.73% |
| `nasa_apod` | 14:00 | 3469.5 | 47.17% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
